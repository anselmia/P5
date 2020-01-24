'''  '''
from models.text import Message

class Favorite():

    def __init__(self, name, id_product, id_substitute):
        self.name
        self.id_product = id_product
        self.id_substitute = id_substitute

    def __str__(self):
        return "product"

    def get_favorite(self, sql, log):
        product = sql.select_where(log,
                                   "product",
                                   ("id",
                                    self.id_product))
        substitute = sql.select_where(log,
                                      "product",
                                      ("id",
                                       self.id_substitute))

        return product, substitute

    @staticmethod
    def get_all_favorites(sql, log):
        """ Method that retrieves products from database. """
        Message.loading(log, "favorite substitutes", "Database")
        favorite_from_db = sql.select(log,
                                      "favorite")

        favorites = []
        for favorite in favorite_from_db:
            favorite_instance = Favorite(favorite[0],
                                         favorite[1])
            favorites.append(favorite_instance)

        if len(favorites) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log,
                                       "favorite substitutes")

        return favorites
