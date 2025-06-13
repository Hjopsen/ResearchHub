import sys

from PySide6 import QtWidgets
from ui.main_ui import MainWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec())