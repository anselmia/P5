from lib.api_com import OpenFoodFactsApi as api
from models.text import Message


class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "category"

    @staticmethod
    def select_from_db(SQL, log):
        """ Method that retrieves categories from database. """
        Message.loading(log, "category", "DataBase")
        database_categories = SQL.select(log, "category")

        categories = []
        for category in database_categories:
            cat = Category(category[1])
            categories.append(cat)

        if len(categories) > 0:
            Message.done(log)
        else:
            Message.load_instead(log, "category")

        return categories

    @staticmethod
    def select_from_api(log):
        """ Method that retrieves categories from open food fact api. """
        Message.loading(log, "category", "API")
        api_categories = api.fetch_categories_data_api(log)

        categories = []
        for category in api_categories:
            cat = Category(category)
            categories.append(cat)

        if len(categories) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log, "categories")

        return categories

    def save_in_db(self, SQL, log):
        category_dic = {"name": self.name}
        return SQL.insert(log, "category", **category_dic)
