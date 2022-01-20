from PyQt6.QtWidgets import QApplication
from bar import Bar
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bar = Bar()
    bar.show()
    sys.exit(app.exec())