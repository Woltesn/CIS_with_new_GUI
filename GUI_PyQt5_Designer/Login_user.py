# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_user.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(191, 263)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(16, 10, 160, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Edit_user_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Edit_user_name.setObjectName("Edit_user_name")
        self.verticalLayout.addWidget(self.Edit_user_name)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Edit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Edit_password.setObjectName("Edit_password")
        self.verticalLayout.addWidget(self.Edit_password)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Edit_repeat_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Edit_repeat_password.setObjectName("Edit_repeat_password")
        self.verticalLayout.addWidget(self.Edit_repeat_password)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 151, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(26, 210, 141, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "User name "))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "Repeat passport"))
        self.pushButton_2.setText(_translate("Form", "Save"))


