from lib.api_com import OpenFoodFactsApi as api


class Category():

    def __init__(self, name=''):
        self.name = name

    @staticmethod
    def select_from_db(SQL, log):
        """ Method that retrieves categories from database. """
        database_categories = SQL.select(log, "category")
        
        categories = []        
        for category in database_categories:
            cat = Category(category[1])
            categories.append(cat)
            
        return categories
    
    @staticmethod
    def select_from_api(log):
        """ Method that retrieves categories from open food fact api. """
        api_categories = api.fetch_categories_data_api(log)
        
        categories = []        
        for category in api_categories:
            cat = Category(category)
            categories.append(cat)
            
        return categories

    @staticmethod
    def save_in_db(SQL, log, category):       
        category_dic = {'name' : category}    
        return SQL.insert(log, 'category', **category_dic)
            
