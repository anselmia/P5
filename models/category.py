from lib.api_com import OpenFoodFactsApi as api


class Category():

    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name


    @staticmethod
    def select_from_db(SQL):
        """ Method that retrieves categories from database. """
        return SQL.select("category")
    
    @staticmethod
    def select_from_api():
        """ Method that retrieves categories from open food fact api. """
        return api.fetch_categories_data_api()

    @staticmethod
    def save_in_db(SQL, categories):            
        for category in categories:   
            category_dic = {'name' : category}    
            SQL.insert('category', **category_dic)
            
