import sys

from PySide6 import QtCore, QtGui, QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("ResearchHub")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        pass
