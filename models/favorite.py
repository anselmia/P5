"""  """
from models.category import Category
from models.product import Product as Prod
from models.text import Message


class Favorite:
    def __init__(self, name, id_product, id_substitute):
        self.name = name
        self.id_product = id_product
        self.id_substitute = id_substitute

    def __str__(self):
        return "product"

    def get_favorite(self, sql, log):
        product_in_db = sql.select_where(log, "product", ("id", self.id_product))
        substitute_in_db = sql.select_where(log, "product", ("id", self.id_substitute))
        
        product_category = sql.select_where(log,
                                            "category",
                                            ("id",
                                             product_in_db[0][10]))
        if len(product_category) > 0:
            product_category_name = product_category[0][1]
            product = Prod(product_in_db[0][1],
                           product_category_name,
                           product_in_db[0][2],
                           product_in_db[0][3],
                           product_in_db[0][4],
                           product_in_db[0][5],
                           product_in_db[0][6],
                           product_in_db[0][7],
                           product_in_db[0][8],
                           product_in_db[0][9])

        substitute_category = sql.select_where(log,
                                               "category",
                                               ("id",
                                                substitute_in_db[0][10]))
        if len(substitute_category) > 0:
            substitute_category_name = substitute_category[0][1]
            substitute = Prod(substitute_in_db[0][1],
                              substitute_category_name,
                              substitute_in_db[0][2],
                              substitute_in_db[0][3],
                              substitute_in_db[0][4],
                              substitute_in_db[0][5],
                              substitute_in_db[0][6],
                              substitute_in_db[0][7],
                              substitute_in_db[0][8],
                              substitute_in_db[0][9])

        return product, substitute

    @staticmethod
    def add_favorite_substitute(sql, log, product, substitute):
        id_product = ""
        id_category = ""

        product_from_db = sql.select_one_attribute_where(
            log, "product", "id", ("name", product.name)
        )
        if len(product_from_db) == 0:
            category_from_db = sql.select_one_attribute_where(
                log, "category", "id", ("name", product.category)
            )
            if len(category_from_db) == 0:
                Message.not_in_db(log, "category : " + product.category)
                category = Category(product.category)
                id_category = category.save_in_db(sql, log)
            else:
                id_category = category_from_db[0][0]

            Message.not_in_db(log, "product : " + product.name)
            id_product = product.save_product_in_db(sql, log, id_category)
        else:
            id_product = product_from_db[0][0]

        id_substitute = ""
        substitute_from_db = sql.select_one_attribute_where(
            log, "product", "id", ("name", substitute.name)
        )
        if len(substitute_from_db) == 0:
            Message.not_in_db(log, "substitute : " + substitute.name)
            id_substitute = substitute.save_product_in_db(sql, log, id_category)
        else:
            id_substitute = substitute_from_db[0][0]

        substitute_dic = {"id_product": id_product, "id_substitute": id_substitute}
        id_substitute = sql.insert(log, "substitute", **substitute_dic)

        return Favorite(substitute.name, id_product, id_substitute)


    @staticmethod
    def get_all_favorites(sql, log):
        """ Method that retrieves products from database. """
        Message.loading(log, "favorite substitutes", "Database")
        favorite_from_db = sql.select(log, "substitute")

        favorites = []
        for favorite in favorite_from_db:
            product_name = sql.select_one_attribute_where(
                log, "product", "name", ("id", favorite[1])
            )
            favorite_instance = Favorite(product_name[0][0], favorite[0], favorite[1])
            favorites.append(favorite_instance)

        if len(favorites) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log, "favorite substitutes")

        return favorites
