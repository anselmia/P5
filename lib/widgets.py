from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem


def add_list_items_to_combobox(combobox, list_items):
    combobox.clear()
    combobox.blockSignals(True)
    combobox.addItems(list_items)
    combobox.blockSignals(False)


def set_tab_column_mode(tab, modes):
    header = tab.horizontalHeader()
    for i in range(len(modes)):
        header.setSectionResizeMode(i, getattr(QHeaderView, modes[i]))


def set_tab_row_header(tab, headers):
    tab.setRowCount(len(headers))
    for row in range(len(headers)):
        # Add following line to only populate first column
        item = QTableWidgetItem(str(headers[row]))
        tab.setItem(row, 0, item)


def populate_tab(tab, obj, attributes):
    for row in range(len(attributes)):
        # Add following line to only populate first column
        item = QTableWidgetItem(str(getattr(obj, attributes[row])))
        tab.setItem(row, 1, item)


def empty_table_column(tab, column_num):
    for row in range(tab.rowCount()):
        item = QTableWidgetItem("")
        tab.setItem(row, column_num, item)
