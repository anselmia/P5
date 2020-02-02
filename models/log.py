""" Module used to redifine the QplainTextEdit appendText method"""

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPlainTextEdit

import settings as CST


class Log(QPlainTextEdit):
    """
        Instance of object QPlainTextEdit Log.
        initilaze with a QPlainTextEdit.
    """

    def __init__(self, text_edit):
        """
            Initialization of the QPlainTextEdit object
            Attributes : QPlainTextEdit
        """
        super().__init__()
        self.text_edit = text_edit
        # Set the background color of the QPlainTextEdit Object
        self.text_edit.setStyleSheet(f"background-color: rgb({CST.PLAIN_TEXT_BACKGROUND_COLOR});")

    def appendText(self, text, color=(0, 255, 0)):
        """
            Append text to the QPlainTextEdit Instance
            arg : text to append
                  color of the text (default = (0, 255, 0))
        """
        color = QColor(*color)
        self.text_edit.setTextColor(color)
        self.text_edit.append(text)
