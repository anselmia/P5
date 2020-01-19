from lib.api_com import OpenFoodFactsApi as api
from models.category import Category as cat


class Product():
    
    def __init__(self, name, category, brands, description, url, nutrition_grade, nutriscore_data):
        self.name = name
        self.category = category
        self.brands = brands
        self.description = description
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.nutriscore_data = nutriscore_data
    
    
    def insert_substitute_in_db(self, SQL, log):        
        id_product = ''
        product_from_db = SQL.select_one_attribute_where(log, "product", 'id', ("name", self.name))       
        if len(product_from_db) == 0:
            id_category = ''
            category_from_db = SQL.select_one_attribute_where(log, "category", 'id', ("name", self.category))       
            if len(category_from_db) == 0:
                id_category = cat.save_in_db(SQL, log, self.category)
            else:
                id_category = category_from_db[0][0]
            
            fat = 0
            if "fat" in self.nutriscore_data:
                fat = self.nutriscore_data["fat"]
            saturated_fat = 0
            if "saturated_fat" in self.nutriscore_data:
                saturated_fat = self.nutriscore_data["saturated_fat"]
            sugar = 0
            if "sugars" in self.nutriscore_data:
                sugar = self.nutriscore_data["sugars"] 
            salt = 0   
            if "salt" in self.nutriscore_data:
                salt = self.nutriscore_data["salt"]    

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
            id_product = SQL.insert(log, 'product', **product_dic)
        else:
            id_product = product_from_db[0][0]
        
        substitute_dic = {"id_product": id_product
                          }    
        id_substitute = SQL.insert(log, 'substitute', **substitute_dic)
          
    def find_substitutes(self, SQL, log, method):
        substitutes = []
        if method == 'API':
            substitutes = self.select_from_api(log, self.category)     
            substitutes = [product for product in substitutes if (product.nutrition_grade == 'a' or product.nutrition_grade == 'b')]       
        else:
            substitutes = self.select_substitute_from_db(SQL, log, self.category)
            if len(substitutes) == 0:
                log.appendText("There is no substitutes in the database within this category. Application will look on the API instead.")
                log.appendText("Loading substitues from API...")
                substitutes = self.select_from_api(log, self.category)     
                substitutes = [product for product in substitutes if (product.nutrition_grade == 'a' or product.nutrition_grade == 'b')]
            
        return substitutes
    
    @staticmethod
    def select_from_api(log, category):
        """ Method that retrieves product from open food fact api. """
        filtered_tags = ['product_name_fr', 'brands', 'url', 'nutrition_grade_fr', 'nutriscore_data']
        api_products = api.fetch_products_data_api(log, category, filtered_tags)
        
        products = []        
        for product in api_products:
            prod = Product(product['product_name_fr'], category, product['brands'], '', product['url'], product['nutrition_grade_fr'], product['nutriscore_data'])
            products.append(prod)
            
        return products
    
    @staticmethod
    def select_from_db(SQL, log, category):
        """ Method that retrieves products from database. """
        category_from_db = SQL.select_one_attribute_where(log, "category", 'id', ("name", category))
        id_category = category_from_db[0][0]
        database_products = SQL.select_where(log, "product", ("id_category", id_category))
    
        products = []        
        for product in database_products:
            prod = Product(product[1], category, product[2], product[3], product[4], product[5], {'fat':product[6],'saturated_fat':product[7],'sugar':product[8], 'salt':product[9]})
            products.append(prod)
        return products
        
    def select_substitute_from_db(self, SQL, log, category):
        """ Method that retrieves substitutes from database. """
        
        category_from_db = SQL.select_where(log, "category", ("name", category))
        id = 1
        if len(category_from_db) == 0:
            return []
        else:        
            select_query = f"SELECT * FROM product WHERE id_category = %s AND (nutrition_grade = %s OR nutrition_grade = %s)"
            values = (id, 'a', 'b')
            return SQL.execute_query(log, select_query, values)