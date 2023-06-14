from PyQt6 import QtCore, QtGui, QtWidgets
import login_page_raw
import socket



def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1120, 936)
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        self.setFont(font)
        self.setStyleSheet("\n"
        "background-color: rgb(211, 211, 211);")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 230, 441, 491))
        self.frame.setStyleSheet("border-radius: 40px;\n"
        "background-color: rgba(180, 180, 180, 175);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 160, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175);\n"
        "border-radius: 10px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 110, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175);\n"
        "border-radius: 10px;  ")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 330, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 370, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(54, 54, 54,175);\n"
        "border-radius: 10px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 420, 151, 24))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(120, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 210, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175);\n"
        "border-radius: 10px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 260, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Multiround Pro")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgba(54, 54, 54,175);\n"
        "border-radius: 10px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Platinum"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "                            Пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "                             Логин"))
        self.checkBox.setText(_translate("MainWindow", "Согласны ли вы с правилами и соглашением Platinum"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton.clicked.connect(lambda: on_reg(self))
        self.pushButton_2.setText(_translate("MainWindow", "Войти"))
        self.pushButton_2.clicked.connect(lambda: login_page_raw.setupUi(self))
        self.label.setText(_translate("MainWindow", "Регистрация"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "          Подтверждение Пароля"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "                             Почта"))

        def on_mouse_click(e):
                if "solid black" in self.lineEdit_2.styleSheet():
                        self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_3.styleSheet():
                        self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_4.styleSheet():
                        self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_5.styleSheet():
                        self.lineEdit_5.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")

        self.frame.mousePressEvent = on_mouse_click

        QtCore.QMetaObject.connectSlotsByName(self)

def on_reg(self):
        login = self.lineEdit_3.text()
        passw = self.lineEdit_2.text()
        email = self.lineEdit_5.text()

        if login == "":

                if "solid black" in self.lineEdit_2.styleSheet():
                        self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_5.styleSheet():
                        self.lineEdit_5.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_4.styleSheet():
                        self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")

                self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black")
                self.passw_empty_wbox = QtWidgets.QMessageBox.warning(self, "Platinum: Login field is empty", "Поле для ввода логина пустое")

        elif passw == "":

                if "solid black" in self.lineEdit_3.styleSheet():
                        self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_5.styleSheet():
                        self.lineEdit_5.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_4.styleSheet():
                        self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")

                self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black")
                self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black")
                self.passw_empty_wbox = QtWidgets.QMessageBox.warning(self, "Platinum: Password field is empty", "Поле для ввода пароля пустое")

        elif "@" not in email or "." not in email:

                if "solid black" in self.lineEdit_3.styleSheet():
                        self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_2.styleSheet():
                        self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                if "solid black" in self.lineEdit_4.styleSheet():
                        self.lineEdit_4.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px;")
                self.lineEdit_5.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black")
                self.passw_empty_wbox = QtWidgets.QMessageBox.warning(self, "Platinum: Email field is empty", "Поле для ввода почты пустое")

        else:


                print("sus")