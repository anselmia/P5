"""This module represent the definition of the object Product."""

from lib.api_com import OpenFoodFactsApi as api


class Product:
    """
    Instance of object Product.
    """

    # List of attributes to show from object
    attributes = [
        "name",
        "brands",
        "url",
        "nutrition_grade",
        "fat",
        "saturated_fat",
        "sugar",
        "salt",
    ]

    # dictionnary to interpret returned object product from database
    # object attribute : DataBase Column Number
    from_db_to_obj = {
        "id": 0,
        "name": 1,
        "brands": 2,
        "url": 3,
        "nutrition_grade": 4,
        "fat": 5,
        "saturated_fat": 6,
        "sugar": 7,
        "salt": 8,
        "id_category": 9,
    }

    def __init__(
        self,
        message,
        name,
        id_category,
        brands,
        url,
        nutrition_grade,
        fat,
        saturated_fat,
        sugar,
        salt,
    ):
        """
        Initialization of the Product object
        Attributes : message instance, name, category's id, brands, url,
        nutrition grade, fat, saturated_fat, sugar, salt
        """
        self.message = message
        self.name = name
        self.id_category = id_category
        self.brands = brands
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.fat = fat
        self.saturated_fat = saturated_fat
        self.sugar = sugar
        self.salt = salt

    def __str__(self):
        """
        Return the name of the object when converting object to string
        """
        return self.name

    def list_attributes_to_show(self):
        """
        Method to get a list of object's attributes from [attributes]
        return a list of attributes
        """
        attributes_to_show = []
        for attribute in self.attributes:
            attributes_to_show.append(str(getattr(self, attribute)))
        return attributes_to_show

    def save_product_in_db(self, sql, id_category):
        """
        Method to save a product in the database
        arg : SQL - Global instance of the sql class
              category'id of the product

        return the id of the inserted product
        """
        self.id_category = id_category
        id_product = sql.insert(
            "product", **{key: self.__dict__[key] for key in self.__dict__ if key != "message"}
        )
        if id_product > 0:
            self.message.saved("product : ", self.name)
        else:
            self.message.exist_in_db("product", self.name)
        return id_product

    def find_substitutes(self, sql, source, category):
        """
        Method to find substitutes to a given product
        arg : SQL - Global instance of the sql class
              source where to search in
              category of the product

              return a list of object Product
        """
        substitutes = []
        if source == "API":
            substitutes = self.select_substitutes_from_api(sql, category)
        else:
            substitutes = self.select_substitute_from_db(sql)
            if len(substitutes) == 0:
                self.message.load_instead("substitute")
                substitutes = self.select_substitutes_from_api(sql, category)

        return substitutes

    def select_substitute_from_db(self, sql):
        """
            Method that retrieves substitutes from database.
            arg : SQL - Global instance of the sql class

            return a list of object Product
        """
        category_from_db = sql.select_where("category", ("id", self.id_category))

        if len(category_from_db) == 0:
            return []
        else:
            # Select where sql query with nutriscore = 'a' or 'b'
            select_query = f"SELECT * FROM product WHERE id_category = %s\
            AND (nutrition_grade = %s OR nutrition_grade = %s)\
            AND (name <> %s)"
            values = (self.id_category, "a", "b", self.name)
            substitutes_from_db = sql.execute_query(select_query, values)

            # List of Product object from list of product's row from database
            substitutes = [
                Product.get_obj_from_db_result(self.message, substitute)
                for substitute in substitutes_from_db
            ]

        if len(substitutes) > 0:
            self.message.done()
        else:
            self.message.impossible_to_load("substitute")

        return substitutes

    def select_substitutes_from_api(self, sql, category):
        """
            Method that retrieves substitutes in the API
            arg : SQL - Global instance of the sql class
                  product's category
            return a list of Product object
        """

        # Products within the same category from the API
        products = self.select_from_api(self.message, sql, category)
        # Filters products with a nutriscore = 'a' or 'b'
        substitutes = [
            product
            for product in products
            if (
                (product.nutrition_grade == "a" or product.nutrition_grade == "b")
                and product.name != self.name
            )
        ]

        return substitutes

    @staticmethod
    def get_obj_from_db_result(message, product_from_db):
        """
        Method that convert product object from database to Product Instance
        arg : product row from db
        return a Product object
        """
        product = Product(
            message,
            product_from_db[Product.from_db_to_obj["name"]],
            product_from_db[Product.from_db_to_obj["id_category"]],
            product_from_db[Product.from_db_to_obj["brands"]],
            product_from_db[Product.from_db_to_obj["url"]],
            product_from_db[Product.from_db_to_obj["nutrition_grade"]],
            product_from_db[Product.from_db_to_obj["fat"]],
            product_from_db[Product.from_db_to_obj["saturated_fat"]],
            product_from_db[Product.from_db_to_obj["sugar"]],
            product_from_db[Product.from_db_to_obj["salt"]],
        )

        return product

    @staticmethod
    def select_from_api(message, sql, category):
        """
            Method that retrieves product from open food fact api.
            arg : SQL - Global instance of the sql class
                  message - Global instance of the text class
                  product's category
            return a list of Product object
        """

        message.loading("product", "API")
        filtered_tags = [
            "product_name_fr",
            "brands",
            "url",
            "nutrition_grade_fr",
            "nutriscore_data",
        ]
        api_products = api.fetch_products_data_api(message, category, filtered_tags)

        products = []
        # Convert list of product's object from API to a list
        # of Product object
        for product in api_products:
            fat = product["nutriscore_data"]["fat"] if "fat" in product["nutriscore_data"] else 0
            saturated_fat = (
                product["nutriscore_data"]["saturated_fat"]
                if "saturated_fat" in product["nutriscore_data"]
                else 0
            )
            sugar = (
                product["nutriscore_data"]["sugars"]
                if "sugars" in product["nutriscore_data"]
                else 0
            )
            salt = (
                product["nutriscore_data"]["salt"] if "salt" in product["nutriscore_data"] else 0
            )

            prod = Product(
                message,
                product["product_name_fr"],
                None,
                product["brands"],
                product["url"],
                product["nutrition_grade_fr"],
                fat,
                saturated_fat,
                sugar,
                salt,
            )
            products.append(prod)

        if len(products) > 0:
            message.done()
        else:
            message.impossible_to_load("product")

        return products

    @staticmethod
    def select_from_db(sql, message, category):
        """
            Method that retrieves products from database.
            arg : SQL - Global instance of the sql class
                  message - Global instance of the text class
                  product's category
            return a list of Product object
        """
        message.loading("product", "Database")

        category_from_db = sql.select_first_row_one_attribute_where(
            "category", "id", ("name", category)
        )
        id_category = category_from_db[Product.from_db_to_obj["id"]]
        database_products = sql.select_where("product", ("id_category", id_category))

        # Convert list of product's object from Database
        # to a list of Product object
        products = [
            Product.get_obj_from_db_result(message, product)
            for product in database_products
            if len(product) == len(Product.from_db_to_obj)
        ]

        if len(products) > 0:
            message.done()
        else:
            message.load_instead("product")

        return products
