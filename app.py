# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog

import lib.widgets as widgets
import settings as CST
from lib.sql_com import SQL
from main import *
from models.category import Category as Cat
from models.favorite import Favorite
from models.log import Log
from models.product import Product as Prod
from models.text import Message


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sql = SQL('localhost',
                       'root',
                       'arnaud06',
                       'open_food_fact')
        self.log = Log(self.ui.te_show)

        self.categories = None
        self.products = None
        self.substitutes = None
        self.favorite_substitutes = Favorite.get_all_favorites(self.sql,
                                                               self.log)
        self.add_favorite_to_combobox()

        self.manage_widgets()

        self.show()

    def add_favorite_to_combobox(self):
        widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_favorite_substitute,
                                                                 self.favorite_substitutes[0:50],
                                                                 'name')

    def manage_widgets(self):
        self.ui.cb_source.addItems(["API",
                                    "DataBase"])

        Message.welcome(self.log)
        self.ui.bt_save_substitute.clicked.connect(self.save_substitute)

        self.ui.bt_last_category.clicked.connect(self.last_category)
        self.ui.bt_next_category.clicked.connect(self.next_category)
        self.ui.bt_last_product.clicked.connect(self.last_product)
        self.ui.bt_next_product.clicked.connect(self.next_product)
        self.ui.bt_last_substitute.clicked.connect(self.last_substitute)
        self.ui.bt_next_substitute.clicked.connect(self.next_substitute)
        self.ui.bt_last_favorite_substitute.clicked.connect(
            self.last_favorite_substitute)
        self.ui.bt_next_favorite_substitute.clicked.connect(
            self.next_favorite_substitute)

        self.ui.cb_source.activated[str].connect(self.select_source)
        self.ui.cb_category.activated[str].connect(self.select_category)
        self.ui.cb_substitute.activated[str].connect(self.select_substitute)
        self.ui.cb_favorite_substitute.activated[str].connect(
            self.select_favorite_substitute)
        self.ui.cb_product.activated[str].connect(self.select_product)

        modes = ["ResizeToContents", "Stretch"]
        widgets.set_tab_column_mode(self.ui.tab_product,
                                    modes)
        widgets.set_tab_column_mode(self.ui.tab_substitute,
                                    modes)

        widgets.set_tab_row_header(self.ui.tab_product,
                                   Prod.attributes)
        widgets.set_tab_row_header(self.ui.tab_substitute,
                                   Prod.attributes)

    def select_source(self, text):
        if text == 'API':
            self.categories = Cat.select_from_api(self.log)
        else:
            self.categories = Cat.select_from_db(self.sql,
                                                 self.log)
            if len(self.categories) == 0:
                self.categories = Cat.select_from_api(self.log)

        if len(self.categories) > 0:
            self.ui.cb_product.clear()
            self.ui.cb_substitute.clear()
            widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_category,
                                                                     self.categories[:CST.NB_OF_CATEGORY_TO_SHOW],
                                                                     'name')
            Message.select(self.log,
                           "category")

    def select_category(self):
        if self.ui.cb_category.count() > 0:
            category = self.ui.cb_category.currentText()
            if self.ui.cb_source.currentText() == 'API':
                self.products = Prod.select_from_api(self.log,
                                                     category)
            else:
                self.products = Prod.select_from_db(self.sql,
                                                    self.log,
                                                    category)
                if len(self.products) == 0:
                    self.products = Prod.select_from_api(self.log,
                                                         category)

            if len(self.products) > 0:
                self.ui.cb_substitute.clear()
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_product,
                                                                         self.products[:CST.NB_OF_PRODUCT_TO_SHOW],
                                                                         'name')
                Message.select(self.log, "product")

    def select_product(self, text):
        if self.ui.cb_product.count() > 0:
            product = next((prod for prod in self.products if prod.name == text), None)
            widgets.populate_tab(self.ui.tab_product,
                                 product,
                                 Prod.attributes)

            self.substitutes = product.find_substitutes(self.sql,
                                                        self.log,
                                                        self.ui.cb_source.currentText())
            if len(self.substitutes) > 0:
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_substitute,
                                                                         self.substitutes[:CST.NB_OF_SUBSTITUTE_TO_SHOW],
                                                                         'name')
                Message.select(self.log, "substitute")

    def select_substitute(self, text):
        if self.ui.cb_product.count() > 0:
            substitute = next((x for x in self.substitutes if x.name == text), None)           
            widgets.populate_tab(self.ui.tab_substitute,
                                 substitute,
                                 Prod.attributes)

    def select_favorite_substitute(self, text):
        if len(self.favorite_substitutes) > 0:
            favorite_substitute = next((x for x in self.favorite_substitutes
                                        if x.name == text), None)
            product, substitute = favorite_substitute.get_favorite(self.sql,
                                                                   self.log)

            if product is not None and substitute is not None:
                widgets.populate_tab(self.ui.tab_product,
                                     product,
                                     Prod.attributes)
                widgets.populate_tab(self.ui.tab_substitute,
                                     substitute,
                                     Prod.attributes)

    def save_substitute(self):
        if len(self.substitutes) > 0 and\
           self.ui.cb_substitute.currentText() != '':

            product = next((prod for prod in self.products
                            if prod.name == self.ui.cb_product.currentText()), None)
            substitute = next((substitute for substitute in self.substitutes
                               if substitute.name == self.ui.cb_substitute.currentText()), None)
            favorite = Favorite.add_favorite_substitute(self.sql,
                                                          self.log,
                                                          product,
                                                          substitute)

            self.favorite_substitutes.append(favorite)
            widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_favorite_substitute,
                                                                     self.favorite_substitutes,
                                                                     'name')

    def next_category(self, text):
        if self.ui.cb_category.count() > 0:
            last_item = self.ui.cb_category.itemText(self.ui.cb_category.count() - 1)
            index_in_list = next((index for index, item in enumerate(self.categories)
                                  if item.name == last_item), -1)

            if index_in_list < len(self.categories) - 1:
                range = self.get_next_range(len(self.categories),
                                            index_in_list,
                                            CST.NB_OF_CATEGORY_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_category,
                                                                         self.categories[range[0]:
                                                                                         range[1]],
                                                                         'name')

    def last_category(self):
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = next((index for index, item in enumerate(self.categories)
                                  if item.name == first_item), -1)

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_CATEGORY_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_category,
                                                                         self.categories[range[0]:
                                                                                         range[1]],
                                                                         'name')

    def next_product(self):
        if self.ui.cb_product.count() > 0:
            last_item = self.ui.cb_product.itemText(self.ui.cb_product.count() - 1)
            index_in_list = next((index for index, item 
                                  in enumerate(self.products)
                                  if item.name == last_item), -1)

            if index_in_list < len(self.products) - 1:
                range = self.get_next_range(len(self.products),
                                            index_in_list,
                                            CST.NB_OF_PRODUCT_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_product,
                                                                         self.products[range[0]:
                                                                                       range[1]],
                                                                         'name')

    def last_product(self):
        if self.ui.cb_product.count() > 0:
            first_item = self.ui.cb_product.itemText(0)
            index_in_list = next((index for index, item
                                  in enumerate(self.products)
                                  if item.name == first_item), -1)

            if index_in_list > 0:
                range = self.get_last_range(index_in_list,
                                            CST.NB_OF_PRODUCT_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_product,
                                                                         self.products[range[0]:
                                                                                       range[1]],
                                                                         'name')

    def next_substitute(self):
        if self.ui.cb_category.count() > 0:
            last_item = self.ui.cb_substitute.itemText(self.ui.cb_substitute.count() - 1)
            index_in_list = next((index for index, item in enumerate(self.substitutes)
                                  if item.name == last_item), -1)

            if index_in_list < len(self.substitutes) - 1:
                range = self.get_next_range(len(self.substitutes),
                                            index_in_list,
                                            CST.NB_OF_SUBSTITUTE_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_substitute,
                                                                         self.substitutes[range[0]:
                                                                                          range[1]],
                                                                         'name')

    def last_substitute(self):
        if self.ui.cb_substitute.count() > 0:
            first_item = self.ui.cb_substitute.itemText(0)
            index_in_list = next((index for index, item in enumerate(self.substitutes)
                                  if item.name == first_item), -1)

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_SUBSTITUTE_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_substitute,
                                                                         self.substitutes[range[0]:
                                                                                          range[1]],
                                                                         'name')

    def next_favorite_substitute(self):
        if self.ui.cb_product.count() > 0:
            last_item = self.ui.cb_product.itemText(self.ui.cb_product.count() - 1)
            product_names = [product.name for product in self.products]
            index_in_list = product_names.index(last_item)

            if index_in_list < len(self.products) - 1:
                range = self.get_next_range(len(self.favorites_substitutes), index_in_list, CST.NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_product,
                                                                         self.favorite_substitutes[range[0]:
                                                                                                   range[1]],
                                                                         'name')

    def last_favorite_substitute(self):
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = self.categories.index(first_item)

            if index_in_list > 0:
                range = self.get_last_range(index_in_list,
                                            CST.NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW)
                widgets.add_items_attribute_to_combobox_from_list_object(self.ui.cb_favorite_substitute,
                                                                         self.favorites_substitutes[range[0]:
                                                                                                    range[1]],
                                                                         'name')

    def get_last_range(index_in_list, item_to_show):
        range = tuple()
        if index_in_list - item_to_show >= 0:
            range = (index_in_list - item_to_show, index_in_list)
        else:
            range = (0, item_to_show)

        return range()

    def get_next_range(self, total_element_in_list, index_in_list, nb_to_show):
        range = tuple()
        if total_element_in_list > index_in_list + nb_to_show:
            range = (index_in_list + 1, index_in_list + nb_to_show + 1)
        else:
            total_element_in_list = len(self.categories)
            range = (total_element_in_list - nb_to_show, total_element_in_list)
        return range


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
