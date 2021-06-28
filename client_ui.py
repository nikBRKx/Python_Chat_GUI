# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 625)
        self.centralwidget = QtWidgets.QWidget(Form)
        #send button
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(10, 470, 300, 28))
        font = QtGui.QFont('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        #send test
        self.sendText = QtWidgets.QLineEdit(Form)
        self.sendText.setGeometry(QtCore.QRect(10, 370, 300, 87))
        self.sendText.setObjectName("sendText")
        font = QtGui.QFont('Arial')
        font.setPointSize(10)
        font.setBold(True)
        self.sendText.setFont(font)
        self.sendText.setPlaceholderText("Enter a message")
        self.sendText.setStyleSheet("background-color: lightgreen")
        #text browser
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.textBrowser.setStyleSheet("background-color: lightgreen")
        font = QtGui.QFont('Arial')
        font.setPointSize(10)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sendButton.setText(_translate("Form", "Send"))

