# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Connect_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(400, 400)
        Form.setFixedSize(400, 200)
        Form.setWindowTitle("Python Retina Chat")

        self.centralwidget = QtWidgets.QWidget(Form)
        #host text
        self.hostText = QtWidgets.QPlainTextEdit(Form)
        self.hostText.setGeometry(QtCore.QRect(160, 40, 145, 30))
        self.hostText.setObjectName("hostText")
        self.hostText.setPlaceholderText('Please enter a hostname')
        #port text
        self.portText = QtWidgets.QPlainTextEdit(Form)
        self.portText.setGeometry(QtCore.QRect(160, 80, 145, 31))
        self.portText.setObjectName("portText")
        self.portText.setPlaceholderText('Please enter a port')
        #nickname text
        self.nicknameText = QtWidgets.QPlainTextEdit(Form)
        self.nicknameText.setGeometry(QtCore.QRect(160, 120, 145, 31))
        self.nicknameText.setObjectName("nicknameText")
        self.nicknameText.setPlaceholderText('Please enter a nickname')
        #host label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 90, 30))
        font = QtGui.QFont('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #port label
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 90, 30))
        font = QtGui.QFont('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #nickname label
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 90, 30))
        font = QtGui.QFont('Arial')
        font.setPointSize(12)
        font.setBold(True)
        #font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #connect button
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(125, 170, 90, 30))
        font = QtGui.QFont('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Host"))
        self.label_2.setText(_translate("Form", "Port"))
        self.label_3.setText(_translate("Form", "Name"))
        self.connectButton.setText(_translate("Form", "Connect"))
        

