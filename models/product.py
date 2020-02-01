from lib.api_com import OpenFoodFactsApi as api
from models.text import Message


class Product:

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
        return self.name

    def save_product_in_db(self, sql, log, id_category):
        self.id_category = id_category
        id_product = sql.insert("product", **self.__dict__)
        if id_product > 0:
            Message.saved(log, "product : ", self.name)
        else:
            Message.exist_in_db(log, "product", self.name)
        return id_product

    def find_substitutes(self, sql, log, method, category):
        substitutes = []
        if method == "API":
            substitutes = self.select_substitutes_from_api(log, sql, category)
        else:
            substitutes = self.select_substitute_from_db(sql, log)
            if len(substitutes) == 0:
                Message.load_instead(log, "substitute")
                substitutes = self.select_substitutes_from_api(log, sql, category)

        return substitutes

    def select_substitute_from_db(self, sql, log):
        """ Method that retrieves substitutes from database."""
        category_from_db = sql.select_where("category", ("id", self.id_category))

        if len(category_from_db) == 0:
            return []
        else:
            id_category = category_from_db[0][0]
            select_query = f"SELECT * FROM product WHERE id_category = %s\
            AND (nutrition_grade = %s OR nutrition_grade = %s)\
            AND (name <> %s)"
            values = (id_category, "a", "b", self.name)
            substitutes_from_db = sql.execute_query(select_query, values)

            substitutes = [
                Product.get_obj_from_db_result(substitute)
                for substitute in substitutes_from_db
            ]

        if len(substitutes) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log, "substitute")

        return substitutes

    def select_substitutes_from_api(self, log, sql, category):
        products = self.select_from_api(log, sql, category)
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
    def get_obj_from_db_result(product_from_db):
        product = Product(
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
    def select_from_api(log, sql, category):
        """ Method that retrieves product from open food fact api. """

        Message.loading(log, "product", "API")
        filtered_tags = [
            "product_name_fr",
            "brands",
            "url",
            "nutrition_grade_fr",
            "nutriscore_data",
        ]
        api_products = api.fetch_products_data_api(log, category, filtered_tags)

        products = []
        for product in api_products:
            fat = (
                product["nutriscore_data"]["fat"]
                if "fat" in product["nutriscore_data"]
                else 0
            )
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
                product["nutriscore_data"]["salt"]
                if "salt" in product["nutriscore_data"]
                else 0
            )

            prod = Product(
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
            Message.done(log)
        else:
            Message.impossible_to_load(log, "product")

        return products

    @staticmethod
    def select_from_db(sql, log, category):
        """ Method that retrieves products from database. """
        Message.loading(log, "product", "Database")

        category_from_db = sql.select_one_attribute_where(
            "category", "id", ("name", category)
        )
        id_category = category_from_db[0][Product.from_db_to_obj["id"]]
        database_products = sql.select_where("product", ("id_category", id_category))

        products = [
            Product.get_obj_from_db_result(product)
            for product in database_products
            if len(product) == len(Product.from_db_to_obj)
        ]

        if len(products) > 0:
            Message.done(log)
        else:
            Message.load_instead(log, "product")

        return products
