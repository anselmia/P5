from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QHeaderView, QTableWidgetItem


def add_list_items_to_combobox(combobox, list_items):
    """
        Add a list of string element to a specified Pyqt ComboBox
        Block the signal of the element while the list is added
    """
    combobox.clear()
    combobox.blockSignals(True)
    combobox.addItems(list_items)
    combobox.blockSignals(False)


def change_combobox_index_from_text(combobox, text_to_find):
    QtCore.QCoreApplication.processEvents()
    index_in_combo = combobox.findText(text_to_find)
    combobox.setCurrentIndex(index_in_combo)
    QtCore.QCoreApplication.processEvents()


def set_tab_column_mode(tab, modes):
    """
        Set the rezised mode of columns header of a specified table pyqt Widget.
        modes is a list of resizing attributes for each column
        ex : ["ResizeToContents", "Stretch"]
    """
    header = tab.horizontalHeader()
    if len(modes) <= tab.columnCount():
        for i in range(len(modes)):
            header.setSectionResizeMode(i, getattr(QHeaderView, modes[i]))


def set_tab_row_header(tab, headers):
    """
        Set the values of the row header of a specified table pyqt Widget.
        headers is a list of string containing values to attributes 
        to headers in row order.
        ex : ["ResizeToContents", "Stretch"]
    """
    tab.setRowCount(len(headers))
    for row in range(len(headers)):
        # Add following line to only populate first column
        item = QTableWidgetItem(str(headers[row]))
        tab.setItem(row, 0, item)


def populate_tab_column(tab, values, col_num):
    """
        Set the values of a given table column number.
    """
    for index, item in enumerate(values):
        # Add following line to only populate first column
        tab_item = QTableWidgetItem(item)
        tab.setItem(index, col_num, tab_item)


def empty_table_column(tab, column_num):
    """
        Set the values to "" of a given table column.
    """
    for row in range(tab.rowCount()):
        item = QTableWidgetItem("")
        tab.setItem(row, column_num, item)
