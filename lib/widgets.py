from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QHeaderView


def add_items_to_combobox(combobox, items):
    combobox.clear()
    combobox.blockSignals(True)
    combobox.addItems(items)
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
            tab.setItem(row,0,item)

def populate_tab(tab, obj, attributes):        
        for row in range(len(attributes)):
            # Add following line to only populate first column
            item = QTableWidgetItem(str(getattr(obj, attributes[row])))
            tab.setItem(row,1,item)