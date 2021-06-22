import PyQt5
from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui
import sys
import socket
import random
from datetime import datetime


class listener(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    running = True

    def __init__(self, client_socket, client):
        # get the parent constructor
        super(listener, self).__init__()
        self.client_socket = client_socket
        self.client = client

    def run(self):
        while self.running:
            self.receive_message()

    def receive_message(self):
        try:
            message = self.client_socket.recv(1024)
            message = message.decode('utf-8')

            #print(message)
            self.signal.emit(message)

        except:
            print("Error 404 - Server not found")
            error = 'Unable to reach server.'
            print('[INFO]', error)
            self.client.show_error('Server Error', error)
            self.running = False



class Client(object):
    def __init__(self):
        #self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()
         # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget.setHidden(True) # chat window not visible
        #chat window 
        self.chat_ui = client_ui.Ui_MainWindow()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.sendButton.clicked.connect(self.send_message)
        self.chat_ui.sendText.returnPressed.connect(self.send_message)
        # connect window
        self.connect_ui = connect_ui.Ui_Connect_Ui()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.connectButton.clicked.connect(self.on_connectButtonClicked)
    
        self.mainWindow.setGeometry(QtCore.QRect(1080, 20,350, 500))
        self.mainWindow.show()
        #create client/user
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            

    def on_connectButtonClicked(self):
        #get host, port and nickname of user
        #function for button in connect window
        host = self.connect_ui.hostText.toPlainText()
        port = self.connect_ui.portText.toPlainText()
        nickname = self.connect_ui.nicknameText.toPlainText()

        if len(host) == 0:
            #if no host entered
            #host = "localhost"
            host = '129.217.162.151'
        if len(port) == 0:
            #if no port entered 
            port = 1337
        else:
            try:
                #correct port entered?
                port = int(port)
            except Exception as e:
                #if port isnt an int
                error = "Invalid port number \n'{}'".format(str(e))
                print("[INFO]", error)
                self.show_error("Port Number Error", error)
        
        if len(nickname) < 1:
            #if no nickname entered
            nickname = socket.gethostname()
            nickname = nickname + "_" + str(random.randint(1, port))

        if self.connect(host, port, nickname): 
            #if self.connect(...) == True
            try:
                self.connectWidget.setHidden(True) #connect window not visible
                self.chatWidget.setVisible(True) #chat window visible

                #start listender Thread to receive msgs
                self.recv_thread = listener(self.client, self)
                self.recv_thread.signal.connect(self.print_message)
                self.recv_thread.start()
                print("[INFO] recv thread started")
            except:
                print('Server offline...')


    def print_message(self, message):
        #print message in chat/textbrowser
        self.chat_ui.textBrowser.append(message)
    
    def connect(self, host, port, nickname):
        #connect client to server
        try:
            self.client.connect((host, port))
            self.client.send(nickname.encode('utf-8'))
            
            print('[INFO] Successfully connected.')
            return True
        except:
            error = 'Unable to connect to Server'
            print('[INFO]', error)
            self.show_error('Connection Error', error)
            self.connect_ui.hostText.clear()
            self.connect_ui.portText.clear()
            
            return False
        
    def send_message(self):
        #send messages from textBox to server
        msg = self.chat_ui.sendText.text().strip()
        if len(msg) == 0:
            return
            
        now = str(datetime.now())[11:16]
        self.chat_ui.textBrowser.append(f'[{now}] - Me: {msg}')
        #print('send: ' + msg)

        try:
            self.client.send(msg.encode('utf-8'))
        except:
            error = 'Unable to send message.'
            print('[INFO]', error)
            self.show_error('Server Error', error)
        
        self.chat_ui.sendText.clear()

    def show_error(self, error_type, msg):
        #error popup 
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(msg)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())