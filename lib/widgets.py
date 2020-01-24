from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QHeaderView
from models.text import Message

def add_items_attribute_to_combobox_from_list_object(combobox, list_objects, attribute_name):
    attributes = [getattr(attribute, attribute_name) for attribute in list_objects]       
                
    combobox.clear()
    combobox.blockSignals(True)
    combobox.addItems(attributes)
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