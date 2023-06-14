from PyQt6 import QtCore, QtGui, QtWidgets
import socket
from reg import setupUi as ui_reg
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QLineEdit

def setupUi(self):
    self.setObjectName("MainWindow")
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    self.setFont(font)
    self.setStyleSheet("background-color: rgb(211, 211, 211);")
    self.centralwidget = QtWidgets.QWidget(parent=self)
    self.centralwidget.setObjectName("centralwidget")
    self.frame = QtWidgets.QFrame(parent=self.centralwidget)
    self.frame.setGeometry(QtCore.QRect(350, 260, 441, 421))
    self.frame.setStyleSheet("border-radius: 40px; background-color: rgba(180, 180, 180, 175);")
    self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.frame.setObjectName("frame")
    self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
    self.lineEdit_2.setGeometry(QtCore.QRect(70, 190, 301, 41))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    self.lineEdit_2.setFont(font)
    self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")
    self.lineEdit_2.setObjectName("lineEdit_2")
    self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
    self.lineEdit_3.setGeometry(QtCore.QRect(70, 140, 301, 41))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    self.lineEdit_3.setFont(font)
    self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")
    self.lineEdit_3.setObjectName("lineEdit_3")
    self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
    self.checkBox.setGeometry(QtCore.QRect(25, 260, 381, 20))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    font.setPointSize(8)
    self.checkBox.setFont(font)
    self.checkBox.setStyleSheet("QCheckBox{background-color: rgba(255, 255, 255, 0); color: #3e403e} QCheckBox::hover{background-color: rgba(255, 255, 255, 0); color: black}")
    self.checkBox.setObjectName("checkBox")
    self.pushButton = QtWidgets.QPushButton(parent=self.frame)
    self.pushButton.setGeometry(QtCore.QRect(130, 300, 171, 31))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    font.setBold(False)
    font.setItalic(False)
    self.pushButton.setFont(font)
    self.pushButton.setStyleSheet("QPushButton{background-color: rgba(72, 72, 72,175); border-radius: 10px;} QPushButton::hover{background-color: rgba(54, 54, 54, 175); border-radius: 10px}")
    self.pushButton.setObjectName("pushButton")
    self.pushButton.clicked.connect(lambda: on_login(self))
    self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
    self.pushButton_2.setGeometry(QtCore.QRect(140, 350, 151, 24))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    font.setPointSize(8)
    self.pushButton_2.setFont(font)
    self.pushButton_2.setStyleSheet("QPushButton{background-color: rgba(72, 72, 72,0); color: #3e403e} QPushButton::hover{background-color: rgba(54, 54, 54, 0); color: black}")
    self.pushButton_2.setObjectName("pushButton_2")
    self.label = QtWidgets.QLabel(parent=self.frame)
    self.label.setGeometry(QtCore.QRect(80, 70, 291, 31))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    font.setPointSize(20)
    self.label.setFont(font)
    self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    self.label.setObjectName("label")
    self.pushButton_2.clicked.connect(lambda: ui_reg(self))
    self.setCentralWidget(self.centralwidget)
    self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
    self.pushButton.setAutoDefault(True)
    self.errorfield = QtWidgets.QLabel(self.frame)
    self.errorfield.setGeometry(QtCore.QRect(120, 30, 300, 16))
    font = QtGui.QFont()
    font.setFamily("Multiround Pro")
    font.setPointSize(9)
    self.errorfield.setFont(font)
    self.errorfield.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    self.errorfield.setObjectName("errorfield")

    def on_mouse_press(e):
        if "solid black" in self.lineEdit_2.styleSheet():
            self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")
        if "solid black" in self.lineEdit_3.styleSheet():
            self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")
        if len(self.errorfield.text()) > 0:
            self.errorfield.setText("")

    self.centralwidget.mousePressEvent = on_mouse_press

    retranslateUi(self)

    QtCore.QMetaObject.connectSlotsByName(self)

def retranslateUi(self):
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("MainWindow", "Platinum"))
    self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "                         Пароль"))
    self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "                          Логин"))
    self.checkBox.setText(_translate("MainWindow", "Согласны ли вы с правилами и соглашением Platinum"))
    self.pushButton.setText(_translate("MainWindow", "Войти"))
    self.pushButton_2.setText(_translate("MainWindow", "Зарегистрироваться"))
    self.label.setText(_translate("MainWindow", "С возвращением!"))

        

def on_login(self):
    login = self.lineEdit_3.text()
    passw = self.lineEdit_2.text()

    if login == "":

        if "solid black" in self.lineEdit_2.styleSheet():
            self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")

        self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black; padding: 10px")
        self.errorfield.setText("Поле для ввода логина пустое")

    elif passw == "":

        if "solid black" in self.lineEdit_3.styleSheet():
            self.lineEdit_3.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; padding: 10px")

        self.lineEdit_2.setStyleSheet("background-color: rgba(54, 54, 54,175); border-radius: 10px; border: 2px solid black; padding: 10px")
        self.errorfield.setText("Поле для ввода пароля пустое")

    
    else:

        if "@" in login:

            sndr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sndr.connect(("localhost", 9999))

            email_line = "on_email_login?" + "|" + login + "|" + passw

            sndr.send(email_line.encode())

        elif "@" not in login:

            sndr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sndr.connect(("localhost", 9999))

            email_line = "on_uname_login?" + "|" + login + "|" + passw

            sndr.send(email_line.encode())
