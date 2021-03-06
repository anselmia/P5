"""Constructor of the main form
This file is generated by Pyqt5
Do not modify"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 553)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_category = QtWidgets.QComboBox(self.centralwidget)
        self.cb_category.setGeometry(QtCore.QRect(10, 80, 341, 22))
        self.cb_category.setEditable(False)
        self.cb_category.setObjectName("cb_category")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bt_next_category = QtWidgets.QPushButton(self.centralwidget)
        self.bt_next_category.setGeometry(QtCore.QRect(150, 50, 31, 20))
        self.bt_next_category.setObjectName("bt_next_category")
        self.bt_last_category = QtWidgets.QPushButton(self.centralwidget)
        self.bt_last_category.setGeometry(QtCore.QRect(120, 50, 31, 20))
        self.bt_last_category.setObjectName("bt_last_category")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_last_product = QtWidgets.QPushButton(self.centralwidget)
        self.bt_last_product.setGeometry(QtCore.QRect(120, 110, 31, 20))
        self.bt_last_product.setObjectName("bt_last_product")
        self.bt_next_product = QtWidgets.QPushButton(self.centralwidget)
        self.bt_next_product.setGeometry(QtCore.QRect(150, 110, 31, 20))
        self.bt_next_product.setObjectName("bt_next_product")
        self.cb_product = QtWidgets.QComboBox(self.centralwidget)
        self.cb_product.setGeometry(QtCore.QRect(10, 140, 341, 22))
        self.cb_product.setEditable(False)
        self.cb_product.setObjectName("cb_product")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cb_source = QtWidgets.QComboBox(self.centralwidget)
        self.cb_source.setGeometry(QtCore.QRect(150, 10, 121, 22))
        self.cb_source.setEditable(False)
        self.cb_source.setObjectName("cb_source")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cb_substitute = QtWidgets.QComboBox(self.centralwidget)
        self.cb_substitute.setGeometry(QtCore.QRect(10, 200, 341, 22))
        self.cb_substitute.setEditable(False)
        self.cb_substitute.setObjectName("cb_substitute")
        self.bt_last_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_last_substitute.setGeometry(QtCore.QRect(120, 170, 31, 20))
        self.bt_last_substitute.setObjectName("bt_last_substitute")
        self.bt_next_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_next_substitute.setGeometry(QtCore.QRect(150, 170, 31, 20))
        self.bt_next_substitute.setObjectName("bt_next_substitute")
        self.cb_favorite_substitute = QtWidgets.QComboBox(self.centralwidget)
        self.cb_favorite_substitute.setGeometry(QtCore.QRect(10, 260, 341, 22))
        self.cb_favorite_substitute.setEditable(False)
        self.cb_favorite_substitute.setObjectName("cb_favorite_substitute")
        self.bt_last_favorite_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_last_favorite_substitute.setGeometry(QtCore.QRect(120, 230, 31, 20))
        self.bt_last_favorite_substitute.setObjectName("bt_last_favorite_substitute")
        self.bt_next_favorite_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_next_favorite_substitute.setGeometry(QtCore.QRect(150, 230, 31, 20))
        self.bt_next_favorite_substitute.setObjectName("bt_next_favorite_substitute")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.bt_save_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save_substitute.setGeometry(QtCore.QRect(860, 10, 51, 23))
        self.bt_save_substitute.setObjectName("bt_save_substitute")
        self.tab_product = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_product.setGeometry(QtCore.QRect(360, 40, 311, 241))
        self.tab_product.setObjectName("tab_product")
        self.tab_product.setColumnCount(2)
        self.tab_product.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_product.setHorizontalHeaderItem(1, item)
        self.tab_substitute = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_substitute.setGeometry(QtCore.QRect(670, 40, 311, 241))
        self.tab_substitute.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tab_substitute.setObjectName("tab_substitute")
        self.tab_substitute.setColumnCount(2)
        self.tab_substitute.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_substitute.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_substitute.setHorizontalHeaderItem(1, item)
        self.te_show = QtWidgets.QTextEdit(self.centralwidget)
        self.te_show.setGeometry(QtCore.QRect(0, 290, 981, 261))
        self.te_show.setFrameShape(QtWidgets.QFrame.Panel)
        self.te_show.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.te_show.setLineWidth(2)
        self.te_show.setReadOnly(True)
        self.te_show.setObjectName("te_show")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Category :"))
        self.bt_next_category.setText(_translate("MainWindow", "Next"))
        self.bt_last_category.setText(_translate("MainWindow", "Last"))
        self.label_2.setText(_translate("MainWindow", "Product :"))
        self.bt_last_product.setText(_translate("MainWindow", "Last"))
        self.bt_next_product.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(_translate("MainWindow", "Select the source :"))
        self.label_4.setText(_translate("MainWindow", "Substitute :"))
        self.bt_last_substitute.setText(_translate("MainWindow", "Last"))
        self.bt_next_substitute.setText(_translate("MainWindow", "Next"))
        self.bt_last_favorite_substitute.setText(_translate("MainWindow", "Last"))
        self.bt_next_favorite_substitute.setText(_translate("MainWindow", "Next"))
        self.label_5.setText(_translate("MainWindow", "My Substitute :"))
        self.label_6.setText(_translate("MainWindow", "Product informations :"))
        self.label_7.setText(_translate("MainWindow", "Substitute informations :"))
        self.bt_save_substitute.setText(_translate("MainWindow", "Save"))
        item = self.tab_product.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Attribute"))
        item = self.tab_product.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tab_substitute.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Attribute"))
        item = self.tab_substitute.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
