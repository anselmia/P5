"""  """
from models.category import Category
from models.product import Product as Prod
from models.text import Message


class Favorite:

    from_db_to_obj = {"id": 0, "id_product": 1, "id_substitute": 2}

    def __init__(self, name, id_product, id_substitute):
        self.name = name
        self.id_product = id_product
        self.id_substitute = id_substitute

    def __str__(self):
        return self.name

    def get_favorite(self, sql, log):
        product_in_db = sql.select_where("product", ("id", self.id_product))
        substitute_in_db = sql.select_where("product", ("id", self.id_substitute))

        product = Prod.get_obj_from_db_result(product_in_db[0])
        substitute = Prod.get_obj_from_db_result(substitute_in_db[0])

        return product, substitute

    @staticmethod
    def add_favorite_substitute(sql, log, category, product, substitute):
        id_product = ""
        id_category = ""

        category_from_db = sql.select_one_attribute_where(
            "category", "id", ("id", product.id_category)
        )
        if len(category_from_db) == 0:
            Message.not_in_db(log, "category : " + category)
            category = Category(category)
            id_category = category.save_in_db(sql, log)
        else:
            id_category = category_from_db[0][0]

        product_from_db = sql.select_one_attribute_where(
            "product", "id", ("name", product.name)
        )
        if len(product_from_db) == 0:
            Message.not_in_db(log, "product : " + product.name)
            id_product = product.save_product_in_db(sql, log, id_category)
        else:
            id_product = product_from_db[0][0]

        id_substitute = ""
        substitute_from_db = sql.select_one_attribute_where(
            "product", "id", ("name", substitute.name)
        )
        if len(substitute_from_db) == 0:
            Message.not_in_db(log, "substitute : " + substitute.name)
            id_substitute = substitute.save_product_in_db(sql, log, id_category)
        else:
            id_substitute = substitute_from_db[0][0]

        substitute_dic = {"id_product": id_product, "id_substitute": id_substitute}
        id_favorite = sql.insert("substitute", **substitute_dic)
        if id_favorite > 0:
            return Favorite(substitute.name, id_product, id_substitute)
        else:
            return None

    @staticmethod
    def get_all_favorites(sql, log):
        """ Method that retrieves products from database. """
        Message.loading(log, "favorite substitutes", "Database")
        favorite_from_db = sql.select("substitute")

        favorites = []
        for favorite in favorite_from_db:
            substitute_name = sql.select_one_attribute_where(
                "product", "name", ("id", favorite[Favorite.from_db_to_obj["id_substitute"]])
            )
            favorite_instance = Favorite(substitute_name[0][0],
                                         favorite[Favorite.from_db_to_obj["id_product"]],
                                         favorite[Favorite.from_db_to_obj["id_substitute"]])
            favorites.append(favorite_instance)

        if len(favorites) > 0:
            Message.done(log)
        else:
            Message.impossible_to_load(log, "favorite substitutes")

        return favorites
