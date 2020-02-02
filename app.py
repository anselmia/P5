# -*- coding: utf-8 -*-
"""
    This module is th main form of the application.
"""

import sys

from PyQt5.QtWidgets import QApplication, QDialog

import lib.widgets as widgets
import settings as CST
from form.main import *
from lib.sql_com import SQL
from models.category import Category as Cat
from models.favorite import Favorite
from models.log import Log
from models.product import Product as Prod
from models.text import Message


class MainWindow(QDialog):
    """
    Instance of the main form.
    """

    def __init__(self):
        """
            Initialization of the main Form
            Initialize : instance of Log class
                         instance of Message Class
                         instance of SQL Class
            Retrieves favorites substitutes in the Database
            initialize all the child Widgets
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.log = Log(self.ui.te_show)
        self.message = Message(self.log)
        self.sql = SQL(self.message)

        self.categories = None
        self.products = None
        self.substitutes = None
        self.favorite_substitutes = Favorite.get_all_favorites(self.sql, self.message)
        self.add_favorite_to_combobox()
        self.manage_widgets()
        self.show()

    def add_favorite_to_combobox(self):
        """
            Add names of favorite_substitutes list to a combobox
        """
        if len(self.favorite_substitutes) > 0:
            favorites_name = [str(favorite) for favorite in self.favorite_substitutes[0:50]]
            widgets.add_list_items_to_combobox(self.ui.cb_favorite_substitute, favorites_name)

    def manage_widgets(self):
        """
            Initialization of all widgets
            Link Widgets to their method's event
        """
        self.ui.cb_source.addItems(["API", "DataBase"])

        Message.welcome(self.message)
        self.ui.bt_save_substitute.clicked.connect(self.save_substitute)

        self.ui.bt_last_category.clicked.connect(self.last_category)
        self.ui.bt_next_category.clicked.connect(self.next_category)
        self.ui.bt_last_product.clicked.connect(self.last_product)
        self.ui.bt_next_product.clicked.connect(self.next_product)
        self.ui.bt_last_substitute.clicked.connect(self.last_substitute)
        self.ui.bt_next_substitute.clicked.connect(self.next_substitute)
        self.ui.bt_last_favorite_substitute.clicked.connect(self.last_favorite_substitute)
        self.ui.bt_next_favorite_substitute.clicked.connect(self.next_favorite_substitute)

        self.ui.cb_source.activated[str].connect(self.select_source)
        self.ui.cb_category.activated[str].connect(self.select_category)
        self.ui.cb_substitute.activated[str].connect(self.select_substitute)
        self.ui.cb_favorite_substitute.activated[str].connect(self.select_favorite_substitute)
        self.ui.cb_product.activated[str].connect(self.select_product)

        modes = ["ResizeToContents", "Stretch"]
        widgets.set_tab_column_mode(self.ui.tab_product, modes)
        widgets.set_tab_column_mode(self.ui.tab_substitute, modes)

        widgets.set_tab_row_header(self.ui.tab_product, Prod.attributes)
        widgets.set_tab_row_header(self.ui.tab_substitute, Prod.attributes)

    def select_source(self, text):
        """
            Method used when cb_source is activated
            Attributes :receive the Actual text in the combobox

            This method retrieves the category depending of the source
            selected by the user.
            Load the category's name in cb_category Combobox
        """
        if text == "API":
            self.categories = Cat.select_from_api(self.message)
        else:
            self.categories = Cat.select_from_db(self.sql, self.message)
            if len(self.categories) == 0:
                self.categories = Cat.select_from_api(self.message)

        if len(self.categories) > 0:
            self.ui.cb_product.clear()
            self.ui.cb_substitute.clear()
            widgets.empty_table_column(self.ui.tab_product, 1)
            widgets.empty_table_column(self.ui.tab_substitute, 1)
            categories_name = [
                str(category) for category in self.categories[: CST.NB_OF_CATEGORY_TO_SHOW]
            ]
            widgets.add_list_items_to_combobox(self.ui.cb_category, categories_name)
            Message.select(self.message, "category")

    def select_category(self):
        """
            Method used when cb_category is activated

            This method retrieves the product depending of the source
            selected by the user.
            Load the product's name in cb_producty Combobox
        """
        if self.ui.cb_category.count() > 0:
            category = self.ui.cb_category.currentText()
            if self.ui.cb_source.currentText() == "API":
                self.products = Prod.select_from_api(self.message, self.sql, category)
            else:
                self.products = Prod.select_from_db(self.sql, self.message, category)
                if len(self.products) == 0:
                    self.products = Prod.select_from_api(self.message, self.sql, category)

            if len(self.products) > 0:
                self.ui.cb_substitute.clear()
                widgets.empty_table_column(self.ui.tab_product, 1)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                products_name = [
                    str(product) for product in self.products[: CST.NB_OF_PRODUCT_TO_SHOW]
                ]
                widgets.add_list_items_to_combobox(
                    self.ui.cb_product, products_name,
                )
                Message.select(self.message, "product")

    def select_product(self, text):
        """
        Method used when cb_product is activated
        Attributes :receive the Actual text in the combobox
        Show the product's attribut in tab_product.
        This method retrieves the substitutes depending of the source
        selected by the user.
        Load the substitute's name in cb_substitute Combobox
        """
        if self.ui.cb_product.count() > 0:
            product = next((prod for prod in self.products if prod.name == text), None)
            widgets.populate_tab_column(self.ui.tab_product, product.list_attributes_to_show(), 1)

            self.substitutes = product.find_substitutes(
                self.sql, self.ui.cb_source.currentText(), self.ui.cb_category.currentText(),
            )
            if len(self.substitutes) > 0:
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                substitutes_name = [
                    str(substitute)
                    for substitute in self.substitutes[: CST.NB_OF_SUBSTITUTE_TO_SHOW]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_substitute, substitutes_name)
                Message.select(self.message, "substitute")

    def select_substitute(self, text):
        """
            Method used when cb_substitute is activated
            Attributes :receive the Actual text in the combobox

            Show selected substitute's attribute in tab_substitute
        """
        if self.ui.cb_product.count() > 0:
            substitute = next((x for x in self.substitutes if x.name == text), None)
            widgets.populate_tab_column(
                self.ui.tab_substitute, substitute.list_attributes_to_show(), 1
            )
            Message.save_substitute(self.message)

    def select_favorite_substitute(self, text):
        """
            Method used when cb_favorite_substitutes is activated
            Attributes :receive the Actual text in the combobox

            Select Database as source an retrieve :
            - category
            - product
            - substitute
            from the database.
            Set all combobox and table according to selected object
        """
        if len(self.favorite_substitutes) > 0:
            favorite_substitute = next(
                (x for x in self.favorite_substitutes if x.name == text), None
            )
            product, substitute = favorite_substitute.get_favorite(self.sql)

            if product is not None and substitute is not None:
                widgets.change_combobox_index_from_text(self.ui.cb_source, "DataBase")
                self.select_source(self.ui.cb_source.currentText())

                category_name = Cat.get_name_from_id(self.sql, product.id_category)
                widgets.change_combobox_index_from_text(self.ui.cb_category, category_name)
                self.select_category()

                widgets.change_combobox_index_from_text(self.ui.cb_product, product.name)
                self.select_product(product.name)

                widgets.change_combobox_index_from_text(self.ui.cb_substitute, substitute.name)
                self.select_substitute(substitute.name)

    def save_substitute(self):
        """
            Method to save favorite substitute in the database

            Select Product from cb_product and convort to Product Object
            Select Substitute from cb_substitute and convort to Substitute (Product) Object

            Add favorite to cb_favorite_substitutes if saved worked
        """
        if len(self.substitutes) > 0 and self.ui.cb_substitute.currentText() != "":

            product = next(
                (prod for prod in self.products if prod.name == self.ui.cb_product.currentText()),
                None,
            )
            substitute = next(
                (
                    substitute
                    for substitute in self.substitutes
                    if substitute.name == self.ui.cb_substitute.currentText()
                ),
                None,
            )
            favorite = Favorite.add_favorite_substitute(
                self.sql, self.message, self.ui.cb_category.currentText(), product, substitute,
            )

            if favorite is not None:
                Message.favorite_saved(self.message)
                self.favorite_substitutes.append(favorite)
                favorites_name = [
                    str(favorite)
                    for favorite in self.favorite_substitutes[
                        : CST.NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW
                    ]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_favorite_substitute, favorites_name)

    def next_category(self):
        """
            Method called when next Category Button is pressed
            Get the index in (list) categories of the last Item in the combobox
            If the index < len(categories) --> Fill the combox with the next items
            using range Tuple
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_category.count() > 0:
            last_item = self.ui.cb_category.itemText(self.ui.cb_category.count() - 1)
            index_in_list = next(
                (index for index, item in enumerate(self.categories) if item.name == last_item),
                -1,
            )

            if (
                index_in_list < len(self.categories) - 1
                and self.ui.cb_category.count() == CST.NB_OF_CATEGORY_TO_SHOW
            ):
                range = self.get_next_range(
                    len(self.categories), index_in_list, CST.NB_OF_CATEGORY_TO_SHOW
                )
                self.ui.cb_product.clear()
                self.ui.cb_substitute.clear()
                widgets.empty_table_column(self.ui.tab_product, 1)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                categories_name = [
                    str(category) for category in self.categories[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_category, categories_name)

    def last_category(self):
        """
            Method called when last Category Button is pressed
            Get the index in (list) categories of the first Item in the combobox
            If the index > 0 --> Fill the combox with the last items
            using range Tuple
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = next(
                (index for index, item in enumerate(self.categories) if item.name == first_item),
                -1,
            )

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_CATEGORY_TO_SHOW)
                self.ui.cb_product.clear()
                self.ui.cb_substitute.clear()
                widgets.empty_table_column(self.ui.tab_product, 1)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                categories_name = [
                    str(category) for category in self.categories[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_category, categories_name)

    def next_product(self):
        """
            Method called when next product Button is pressed
            Get the index in (list) products of the last Item in the combobox
            If the index < len(products) --> Fill the combox with the next items
            using range Tuple.
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_product.count() > 0:
            last_item = self.ui.cb_product.itemText(self.ui.cb_product.count() - 1)
            index_in_list = next(
                (index for index, item in enumerate(self.products) if item.name == last_item), -1,
            )

            if (
                index_in_list < len(self.products) - 1
                and self.ui.cb_category.count() == CST.NB_OF_CATEGORY_TO_SHOW
            ):
                range = self.get_next_range(
                    len(self.products), index_in_list, CST.NB_OF_PRODUCT_TO_SHOW
                )
                self.ui.cb_substitute.clear()
                widgets.empty_table_column(self.ui.tab_product, 1)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                products_name = [str(product) for product in self.products[range[0] : range[1]]]
                widgets.add_list_items_to_combobox(self.ui.cb_product, products_name)

    def last_product(self):
        """
            Method called when last products Button is pressed
            Get the index in (list) productss of the first Item in the combobox
            If the index > 0 --> Fill the combox with the last items
            using range Tuple
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_product.count() > 0:
            first_item = self.ui.cb_product.itemText(0)
            index_in_list = next(
                (index for index, item in enumerate(self.products) if item.name == first_item), -1,
            )

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_PRODUCT_TO_SHOW)
                self.ui.cb_substitute.clear()
                widgets.empty_table_column(self.ui.tab_product, 1)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                products_name = [str(product) for product in self.products[range[0] : range[1]]]
                widgets.add_list_items_to_combobox(self.ui.cb_product, products_name)

    def next_substitute(self):
        """
            Method called when next Substitute Button is pressed
            Get the index in (list) substitutes of the last Item in the combobox
            If the index < len(substitutes) --> Fill the combox with the next items
            using range Tuple.
            Amount of items showed can be configured in the settings
        """
        if (
            self.ui.cb_category.count() > 0
            and self.ui.cb_category.count() == CST.NB_OF_CATEGORY_TO_SHOW
        ):
            last_item = self.ui.cb_substitute.itemText(self.ui.cb_substitute.count() - 1)
            index_in_list = next(
                (index for index, item in enumerate(self.substitutes) if item.name == last_item),
                -1,
            )

            if index_in_list < len(self.substitutes) - 1:
                range = self.get_next_range(
                    len(self.substitutes), index_in_list, CST.NB_OF_SUBSTITUTE_TO_SHOW
                )
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                substitutes_name = [
                    str(substitute) for substitute in self.substitutes[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_substitute, substitutes_name)

    def last_substitute(self):
        """
            Method called when last Substitute Button is pressed
            Get the index in (list) substitutes of the first Item in the combobox
            If the index > 0 --> Fill the combox with the last items
            using range Tuple
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_substitute.count() > 0:
            first_item = self.ui.cb_substitute.itemText(0)
            index_in_list = next(
                (index for index, item in enumerate(self.substitutes) if item.name == first_item),
                -1,
            )

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_SUBSTITUTE_TO_SHOW)
                widgets.empty_table_column(self.ui.tab_substitute, 1)
                substitutes_name = [
                    str(substitute) for substitute in self.substitutes[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_substitute, substitutes_name)

    def next_favorite_substitute(self):
        """
            Method called when next Favorite Substitutes Button is pressed
            Get the index in (list) favorite_substitutes of the last Item in the combobox
            If the index < len(favorite_substitutes) --> Fill the combox with the next items
            using range Tuple.
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_favorite_substitute.count() > 0:
            last_item = self.ui.cb_favorite_substitute.itemText(
                self.ui.cb_favorite_substitute.count() - 1
            )
            favorites_names = [favorite.name for favorite in self.favorite_substitutes]
            index_in_list = next(
                (
                    index
                    for index, item in enumerate(self.favorite_substitutes)
                    if item.name == last_item
                ),
                -1,
            )

            if index_in_list < len(self.favorite_substitutes) - 1:
                range = self.get_next_range(
                    len(self.favorite_substitutes),
                    index_in_list,
                    CST.NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW,
                )
                favorites_name = [
                    str(favorite) for favorite in self.favorite_substitutes[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_favorite_substitute, favorites_name)

    def last_favorite_substitute(self):
        """
            Method called when last Favorite Substitutes Button is pressed
            Get the index in (list) favorite_substitutes of the first Item in the combobox
            If the index > 0 --> Fill the combox with the last items
            using range Tuple
            Amount of items showed can be configured in the settings
        """
        if self.ui.cb_favorite_substitute.count() > 0:
            first_item = self.ui.cb_favorite_substitute.itemText(0)
            index_in_list = next(
                (
                    index
                    for index, item in enumerate(self.favorite_substitutes)
                    if item.name == first_item
                ),
                -1,
            )

            if index_in_list > 0:
                range = self.get_last_range(index_in_list, CST.NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW)
                favorites_name = [
                    str(favorite) for favorite in self.favorite_substitutes[range[0] : range[1]]
                ]
                widgets.add_list_items_to_combobox(self.ui.cb_favorite_substitute, favorites_name)

    def get_last_range(self, index_in_list, item_to_show):
        """
            Generic method to recalculate the last range
            arg : index_in_list of the first item (int)
                  number of items to show
        """
        range = tuple()
        if index_in_list - item_to_show >= 0:
            range = (index_in_list - item_to_show, index_in_list)
        else:
            range = (0, item_to_show)

        return range

    def get_next_range(self, total_element_in_list, index_in_list, nb_to_show):
        """
            Generic method to recalculate the next range
            arg : index_in_list of the last item (int)
                  number of items to show
        """
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
