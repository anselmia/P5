from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPlainTextEdit

import settings as CST


class Log(QPlainTextEdit):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.text_edit.setStyleSheet(
            f"background-color: rgb({CST.PLAIN_TEXT_BACKGROUND_COLOR});"
        )

    def appendText(self, text, color=(0, 255, 0)):
        color = QColor(*color)
        self.text_edit.setTextColor(color)
        self.text_edit.append(text)
