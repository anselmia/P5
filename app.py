from lib.api_com import OpenFoodFactsApi as api
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from main import *
from models.category import Category as Cat
from models.product import Product as Prod
from models.log import Log
from lib.sql_com import SQL
import settings as CST
import lib.widgets as widgets


class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.log = Log(self.ui.te_show) 
        self.manage_widgets()        
        
        self.show()
        self.SQL = SQL('localhost', 'root', 'arnaud06', 'open_food_fact')
        
        self.categories = None
        self.products = None
        self.substitute = None
    
    def manage_widgets(self):          
        self.ui.cb_source.addItems(["API","DataBase"])
        
        self.log.appendText("Welcome\nPlease select a source to start.\n")
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
        self.ui.cb_favorite_substitute.activated.connect(self.select_favorite_substitute)
        self.ui.cb_product.activated[str].connect(self.select_product)
        
        modes = ["ResizeToContents", "Stretch"]
        widgets.set_tab_column_mode(self.ui.tab_product, modes)
        widgets.set_tab_column_mode(self.ui.tab_substitute, modes)
        
        rows = ['name', 'brands', 'url', 'grade']
        widgets.set_tab_row_header(self.ui.tab_product, rows)
        widgets.set_tab_row_header(self.ui.tab_substitute, rows)

    def select_source(self, text):
        if text == 'API':
            self.log.appendText("Loading categories from API...")
            self.categories = Cat.select_from_api(self.log)            
        else:
            self.log.appendText("Loading categories from Database...")
            self.categories = Cat.select_from_db(self.SQL, self.log)
            if len(self.categories) == 0:
                self.log.appendText("There is no category in the database. Application will look on the API instead.")
                self.log.appendText("Loading categories from API...")
                self.categories = Cat.select_from_api(self.log)

        if len(self.categories) > 0:
            categories_name = [category.name for category in self.categories]
            widgets.add_items_to_combobox(self.ui.cb_category, categories_name[:CST.NB_OF_CATEGORY_TO_SHOW])   
            self.log.appendText("Done")
   
    def select_category(self):
        if self.ui.cb_category.count() > 0:
            category = self.ui.cb_category.currentText()
            if self.ui.cb_source.currentText() == 'API':
                self.log.appendText("Loading product from API...")
                self.products = Prod.select_from_api(self.log, category)       
            else:      
                self.log.appendText("Loading products from Database...")
                self.products = Prod.select_from_db(self.SQL, self.log, category)
                if len(self.products) == 0:
                    self.log.appendText("There is no products in the database within this category. Application will look on the API instead.")
                    self.log.appendText("Loading products from API...")
                    self.products = Prod.select_from_api(self.log, category)
                    self.log.appendText("Done...")
                
            product_names = [product.name for product in self.products]
            widgets.add_items_to_combobox(self.ui.cb_product, product_names[:CST.NB_OF_PRODUCT_TO_SHOW])
            
            self.log.appendText("Please select a product")
            
    def select_product(self, text):
        if self.ui.cb_product.count() > 0:
            product = next((x for x in self.products if x.name == text), None)
            attributes = ['name', 'brands', 'url', 'nutrition_grade']
            widgets.populate_tab(self.ui.tab_product, product, attributes)
            self.substitutes = product.find_substitutes(self.SQL, self.log, self.ui.cb_source.currentText())
            substitutes_names = [product.name for product in self.substitutes]
            widgets.add_items_to_combobox(self.ui.cb_substitute, substitutes_names[:CST.NB_OF_SUBSTITUTE_TO_SHOW])
            
            self.log.appendText("Please select a substitute")
    
    def select_substitute(self, text):
        if self.ui.cb_product.count() > 0:
            substitute = next((x for x in self.substitutes if x.name == text), None)
            attributes = ['name', 'brands', 'url', 'nutrition_grade']
            widgets.populate_tab(self.ui.tab_substitute, substitute, attributes)
    
    def select_favorite_substitute(self):
        pass
    
    def save_substitute(self):
        if len(self.products) > 0 and self.ui.cb_substitute.currentText() != '':
            product = next((product for product in self.products if product.name == self.ui.cb_product.currentText()), None)
            product.insert_substitute_in_db(self.SQL, self.log)

    def next_category(self, text):
        if self.ui.cb_category.count() > 0:      
            last_item = self.ui.cb_category.itemText(self.ui.cb_category.count() - 1)
            index_in_list = self.categories.index(last_item)
            
            if index_in_list < len(self.categories) - 1:
                if len(self.categories) > index_in_list + CST.NB_OF_CATEGORY_TO_SHOW:
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[index_in_list + 1 : index_in_list + CST.NB_OF_CATEGORY_TO_SHOW + 1])
                else:
                    total_element_in_list = len(self.categories)
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[total_element_in_list - CST.NB_OF_CATEGORY_TO_SHOW : total_element_in_list])
    
    def last_category(self):
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = self.categories.index(first_item)
            
            if index_in_list > 0:
                if index_in_list - CST.NB_OF_CATEGORY_TO_SHOW >=0 :
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[index_in_list - CST.NB_OF_CATEGORY_TO_SHOW : index_in_list])
                else:
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[0 : CST.NB_OF_CATEGORY_TO_SHOW])
        
    def next_product(self):
        if self.ui.cb_product.count() > 0:      
            last_item = self.ui.cb_product.itemText(self.ui.cb_product.count() - 1)
            product_names = [product.name for product in self.products]
            index_in_list = product_names.index(last_item)
            
            if index_in_list < len(self.products) - 1:
                if len(self.products) > index_in_list + CST.NB_OF_PRODUCT_TO_SHOW:
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[index_in_list + 1 : index_in_list + CST.NB_OF_PRODUCT_TO_SHOW + 1])
                else:
                    total_element_in_list = len(self.products)
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[total_element_in_list - CST.NB_OF_PRODUCT_TO_SHOW : total_element_in_list])

    def last_product(self):
        if self.ui.cb_product.count() > 0:            
            first_item = self.ui.cb_product.itemText(0)
            product_names = [product.name for product in self.products]
            index_in_list = product_names.index(first_item)
            
            if index_in_list > 0:
                if index_in_list - CST.NB_OF_PRODUCT_TO_SHOW >=0 :
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[index_in_list - CST.NB_OF_PRODUCT_TO_SHOW : index_in_list])
                else:
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[0 : CST.NB_OF_PRODUCT_TO_SHOW])

    def next_substitute(self):
        if self.ui.cb_category.count() > 0:      
            last_item = self.ui.cb_category.itemText(self.ui.cb_category.count() - 1)
            index_in_list = self.categories.index(last_item)
            
            if index_in_list < len(self.categories) - 1:
                if len(self.categories) > index_in_list + CST.NB_OF_CATEGORY_TO_SHOW:
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[index_in_list + 1 : index_in_list + CST.NB_OF_CATEGORY_TO_SHOW + 1])
                else:
                    total_element_in_list = len(self.categories)
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[total_element_in_list - CST.NB_OF_CATEGORY_TO_SHOW : total_element_in_list])
    
    def last_substitute(self):
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = self.categories.index(first_item)
            
            if index_in_list > 0:
                if index_in_list - CST.NB_OF_CATEGORY_TO_SHOW >=0 :
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[index_in_list - CST.NB_OF_CATEGORY_TO_SHOW : index_in_list])
                else:
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[0 : CST.NB_OF_CATEGORY_TO_SHOW])
        
    def next_favorite_substitute(self):
        if self.ui.cb_product.count() > 0:      
            last_item = self.ui.cb_product.itemText(self.ui.cb_product.count() - 1)
            product_names = [product.name for product in self.products]
            index_in_list = product_names.index(last_item)
            
            if index_in_list < len(self.products) - 1:
                if len(self.products) > index_in_list + CST.NB_OF_PRODUCT_TO_SHOW:
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[index_in_list + 1 : index_in_list + CST.NB_OF_PRODUCT_TO_SHOW + 1])
                else:
                    total_element_in_list = len(self.products)
                    widgets.add_items_to_combobox(self.ui.cb_product, product_names[total_element_in_list - CST.NB_OF_PRODUCT_TO_SHOW : total_element_in_list])

    def last_favorite_substitute(self):
        if self.ui.cb_category.count() > 0:
            first_item = self.ui.cb_category.itemText(0)
            index_in_list = self.categories.index(first_item)
            
            if index_in_list > 0:
                if index_in_list - CST.NB_OF_CATEGORY_TO_SHOW >=0 :
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[index_in_list - CST.NB_OF_CATEGORY_TO_SHOW : index_in_list])
                else:
                    widgets.add_items_to_combobox(self.ui.cb_category, self.categories[0 : CST.NB_OF_CATEGORY_TO_SHOW])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
