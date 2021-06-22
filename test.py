from PyQt5 import QtCore, QtGui
import sys


import PyQt5
from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui

import sys
import socket
import random
from datetime import datetime



class MainWindow(object):
    def __init__(self):
        super.__init__()
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.test()
    def test(self):
        print("space pressed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    demo = MainWindow()
    
    sys.exit(app.exec_())
