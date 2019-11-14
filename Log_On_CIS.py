# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_On_CIS.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, LoginUser):
        LoginUser.setObjectName("LoginUser")
        LoginUser.resize(340, 351)
        self.centralwidget = QtWidgets.QWidget(LoginUser)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 321, 31))
        self.pushButton.setStyleSheet("font: 14pt \"Times New Roman\"; \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 61, 21))
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 111, 21))
        self.label_2.setStyleSheet("font: 14pt \"Arial\";\n"
"font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 240, 131, 17))
        self.checkBox.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 200, 321, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 321, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 181, 16))
        self.label_4.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";\n"
"font: 14pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 50, 31, 23))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        LoginUser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginUser)
        self.statusbar.setObjectName("statusbar")
        LoginUser.setStatusBar(self.statusbar)

        self.retranslateUi(LoginUser)
        QtCore.QMetaObject.connectSlotsByName(LoginUser)

    def retranslateUi(self, LoginUser):
        _translate = QtCore.QCoreApplication.translate

        LoginUser.setWindowTitle(_translate("LoginUser", "CIS application"))
        self.pushButton.setText(_translate("LoginUser", "Log in"))
        self.label.setText(_translate("LoginUser", "Log In"))
        self.label_2.setText(_translate("LoginUser", "Password"))
        self.checkBox.setText(_translate("LoginUser", "remember me"))
        self.label_4.setText(_translate("LoginUser", "New use? Create an account "))
        self.label_5.setText(_translate("LoginUser", "User name "))
        self.pushButton_2.setText(_translate("LoginUser", "start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginUser = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(LoginUser)
    LoginUser.show()
    sys.exit(app.exec_())
