from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
import sys
import login_page_raw

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowIcon(QIcon("/home/tscrt/Desktop/platinum/icon.png"))
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1600, 900)
        login_page_raw.setupUi(self)

app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())