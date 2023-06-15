from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
import sys
import login_page_raw

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowIcon(QIcon("/home/tscrt/Desktop/platinum/icon.png"))
        self.setMinimumSize(1110, 868)
        self.setMaximumSize(1390, 868)
        self.setWindowTitle("Platinum")
        login_page_raw.on_checking(self)

app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())