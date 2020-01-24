from lib.api_com import OpenFoodFactsApi as api
from models.category import Category
from models.text import Message
from models.favorite import Favorite

class Product():

    attributes = ['name',
                  'brands',
                  'url',
                  'nutrition_grade',
                  'fat',
                  'saturated_fat',
                  'sugar',
                  'salt']

    def __init__(self, name, category, brands, description, url, nutrition_grade,\
                 fat, saturated_fat, sugar, salt):
        self.name = name
        self.category = category
        self.brands = brands
        self.description = description
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.fat = fat
        self.saturated_fat = saturated_fat
        self.sugar = sugar
        self.salt = salt

    def __str__(self):
        return "product"

    def add_favorite_substitute(self, sql, log, product):
        id_product = ''
        id_category = ''

        product_from_db = sql.select_one_attribute_where(log,
                                                         "product",
                                                         'id',
                                                         ("name",
                                                          product.name))
        if len(product_from_db) == 0:
            category_from_db = sql.select_one_attribute_where(log,
                                                              "category",
                                                              'id',
                                                              ("name",
                                                               product.category))
            if len(category_from_db) == 0:
                Message.not_in_db(log, "category : " + product.category)
                category = Category(product.category)
                id_category = category.save_in_db(sql,
                                                  log)
            else:
                id_category = category_from_db[0][0]

            Message.not_in_db(log, "product : " + product.name)
            id_product = product.save_product_in_db(sql, log, id_category)

        id_substitute = ''
        substitute_from_db = sql.select_one_attribute_where(log,
                                                            "product",
                                                            'id',
                                                            ("name",
                                                             self.name))
        if len(substitute_from_db) == 0:
            Message.not_in_db(log, "substitute : " + self.name)
            id_substitute = self.save_product_in_db(sql,
                                                    log,
                                                    id_category)
        else:
            id_substitute = substitute_from_db[0][0]

        substitute_dic = {"id_product": id_product, "id_substitute":id_substitute}
        id_substitute = sql.insert(log, 'substitute', **substitute_dic)

        return Favorite(self.name, id_product, id_substitute)

    def save_product_in_db(self, sql, log, id_category):
        fat = self.nutriscore_data["fat"]\
              if "fat" in self.nutriscore_data else 0
        saturated_fat = self.nutriscore_data["saturated_fat"]\
                        if "saturated_fat" in self.nutriscore_data else 0
        sugar = self.nutriscore_data["sugars"] if "sugars" in self.nutriscore_data else 0
        salt =  self.nutriscore_data["salt"] if "salt" in self.nutriscore_data else 0

        product_dic = {"name" : self.name,
                       "id_category": id_category,
                       "brands": self.brands,
                       "description": self.description,
                       "url": self.url,
                       "nutrition_grade": self.nutrition_grade,
                       "fat": fat,
                       "saturated_fat": saturated_fat,
                       "salt": salt,
                       "sugar": sugar
                       }    

        id_product = sql.insert(log, 'product', **product_dic)
        if(id_product > 0):
            Message.saved(log, "product : ", self.name)
        else:
            Message.exist_in_db(log, "product", self.name)
        return id_product

    def find_substitutes(self, sql, log, method):
        substitutes = []
        if method == 'API':
            substitutes = self.select_from_api(log, self.category)
            substitutes = [product for product in substitutes 
                           if (product.nutrition_grade == 'a' or product.nutrition_grade == 'b')]       
        else:
            substitutes = self.select_substitute_from_db(sql, log, self.category)
            if len(substitutes) == 0:
                Message.load_instead(log, "substitute")
                substitutes = self.select_from_api(log, self.category)
                if len(substitutes) > 0:
                    substitutes = [product for product in substitutes 
                                   if (product.nutrition_grade == 'a' or product.nutrition_grade == 'b')]

        return substitutes

    @staticmethod
    def select_from_api(log, category):
        """ Method that retrieves product from open food fact api. """

        Message.loading(log,
                        "product",
                        "API")
        filtered_tags = ['product_name_fr',
                         'brands',
                         'url',
                         'nutrition_grade_fr',
                         'nutriscore_data']
        api_products = api.fetch_products_data_api(log,
                                                   category,
                                                   filtered_tags)

        products = []        
        for product in api_products:
            fat = product['nutriscore_data']["fat"]\
                  if "fat" in product['nutriscore_data'] else 0
            saturated_fat = product['nutriscore_data']["saturated_fat"]\
                            if "saturated_fat" in product['nutriscore_data'] else 0
            sugar = product['nutriscore_data']["sugars"]\
                    if "sugars" in product['nutriscore_data'] else 0
            salt =  product['nutriscore_data']["salt"]\
                    if "salt" in product['nutriscore_data'] else 0

            prod = Product(product['product_name_fr'],
                           category,
                           product['brands'],
                           '',
                           product['url'],
                           product['nutrition_grade_fr'],
                           fat,
                           saturated_fat,
                           sugar,salt)
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

        category_from_db = sql.select_one_attribute_where(log, "category", 'id', ("name", category))
        id_category = category_from_db[0][0]
        database_products = sql.select_where(log, "product", ("id_category", id_category))

        products = []        
        for product in database_products:
            prod = Product(product[1], category, product[2], product[3], product[4], product[5], product[6], product[7], product[8], product[9])
            products.append(prod)

        if len(products) > 0:
            Message.done(log)
        else:
            Message.load_instead(log, "product")

        return products

    def select_substitute_from_db(self, sql, log, category):
        """ Method that retrieves substitutes from database."""
        category_from_db = sql.select_where(log, "category", ("name", category))
       
        if len(category_from_db) == 0:
            return []
        else:        
            id_category = category_from_db[0][0]
            select_query = f"SELECT * FROM product WHERE id_category = %s AND (nutrition_grade = %s OR nutrition_grade = %s)"
            values = (id_category, 'a', 'b')
            substitutes_from_db = sql.execute_query(log, select_query, values)

            substitutes = []        
            for substitute in substitutes_from_db:
                subst = Product(substitute[1],
                                category,
                                substitute[2],
                                substitute[3],
                                substitute[4],
                                substitute[5],
                                substitute[6],
                                substitute[7],
                                substitute[8],
                                substitute[9])
                substitutes.append(subst)

        if len(substitutes) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log, "substitute")

        return substitutes
