from lib.api_com import OpenFoodFactsApi as api
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from main import *
from models.category import Category as Cat
from lib.sql_com import SQL
#from window import Window 

class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pte_show.appendPlainText("Welcome\n\n")
        self.ui.bt_substitute.clicked.connect(self.substitute)
        #self.ui.cb_category.currentIndexChanged(self.select_cat)
        self.show()
        self.SQL = SQL('localhost', 'root', 'arnaud06', 'open_food_fact')
    
    def substitute(self):
        categories = Cat.select_from_db(self.SQL)
        if len(categories) < 2:
            categories = Cat.select_from_api()
            if len(categories) != 0:
                Cat.save_in_db(self.SQL, categories)#print cat in cb_category

    def select_cat(self):
        if self.ui.cb_category.count() > 0:
            if self.ui.cb_category.currentIndex != 0:
                set_cb_product(self.ui.cb_category.currentIndex)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
