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
        MainWindow.resize(801, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_substitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_substitute.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.bt_substitute.setObjectName("bt_substitute")
        self.pte_show = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pte_show.setGeometry(QtCore.QRect(250, 0, 551, 481))
        self.pte_show.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pte_show.setReadOnly(True)
        self.pte_show.setObjectName("pte_show")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.bt_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.bt_confirm.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.bt_confirm.setObjectName("bt_confirm")
        self.bt_mysubstitute = QtWidgets.QPushButton(self.centralwidget)
        self.bt_mysubstitute.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.bt_mysubstitute.setObjectName("bt_mysubstitute")
        self.cb_category = QtWidgets.QComboBox(self.centralwidget)
        self.cb_category.setGeometry(QtCore.QRect(10, 150, 231, 22))
        self.cb_category.setEditable(False)
        self.cb_category.setObjectName("cb_category")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label.setObjectName("label")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_substitute.setText(_translate("MainWindow", "Substitute"))
        self.bt_confirm.setText(_translate("MainWindow", "Confirm"))
        self.bt_mysubstitute.setText(_translate("MainWindow", "My Substitute"))
        self.label.setText(_translate("MainWindow", "Category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
