import socket
import threading
from datetime import datetime
import os
host = '129.217.162.151'
port = 1337

#dictionary for clients
clients = {}

#get directory for correct path (history.txt)
directory = os.path.dirname(__file__)  

#create server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()




def broadcast(message, sender):
    #sends msgs to all clients 
    if len(clients) > 0:
        for nickname in clients:
            if nickname != sender:
                now = str(datetime.now())[11:16]
                msg = f'[{now}] - {sender}: {message}'
                clients[nickname].send(msg.encode('utf-8'))


def broadcast_admin(message):
    #sends nonuser messages
    for nickname in clients:
        clients[nickname].send(message.encode('utf-8'))

def write_history(message, nickname): 
    # funktion, die den chatverlauf in eine txt schreibt
    try: 
        history = open(directory + '/history.txt', 'a')
        now = str(datetime.now())[11:16]
        history.write(f'[{now}] - {nickname}: {str(message)}\n') # schreibe die messages der clients nacheinander in die txt
    except:
        print('[Admin] Could not write chat history')


def handle_client(client, nickname):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')

            #if len(message) >= 4 and message[0:9] == "/private ": # falls /private nickname dann private messsage // slicing betrachtet die zeichen des strings // private hat 8 zeichen
            if msg[0:9] == "/private ":
                split = msg.split(" ")
                # /private niklas hallo
                # ["/private", "niklas", "hallo"] <-- so ist message als string aufgebaut nach split methode
                username = split[1]
                if username in clients:
                    receiver = clients[username]
                    now = str(datetime.now())[11:16]
                    #join ist gegensatz zu split und setzt nachricht weider zu einem string zusammen
                    receiver.send(f'[{now}] - {nickname} (private): {" ".join(split[2:])}'.encode("utf-8"))
                else:
                    client.send("[Admin] Username not valid.".encode('utf-8'))  
            elif msg == '!help':
                client.send('[Admin] To send a private message please enter: /private username \n'.encode('utf-8'))
                client.send('[Admin] To see users currently online please enter: !users \n'.encode('utf-8'))
            elif msg == '!users':
                #get current users
                users = clients.keys()
                client.send(f'[Admin] Currently online in chat: '.encode('utf-8'))
                for user in users:
                    client.send(f'{user} \n'.encode('utf-8'))
            else:
                #if no private msg then broadcast to everyone and write chat history
                broadcast(msg, nickname)
                write_history(msg, nickname)
                
        except:
            #if no connection to client
            client.close()  
            del(clients[nickname])
            break
    broadcast_admin(f'{nickname} left the chat.')
    print(f'[Admin] {nickname} disconnected.')

#main function 
def receive():
    while True:
        #get client information
        client, address = server.accept()
        print('[Admin] Connected with '+ str(address))

        #get entered nickname and add to dictionary
        nickname = client.recv(1024).decode('utf-8')
        #nickname = nickname.decode('utf-8')
        clients[nickname] = client
        #print(clients)
        print(f'[Admin] Nickname  of client {address[1]} is {nickname}')
        broadcast_admin(f'[Admin] {nickname} joined the chat!')

        #chat history
        try:
            with open(directory + '/history.txt','r') as text_file:
                history = text_file.read()
        except FileNotFoundError:
            print(f'[Admin] New history.txt created...')
            open(directory + '/history.txt','a')
            with open(directory + '/history.txt','r') as text_file:
                history = text_file.read()
        #send chat history to client
        client.send('Previous chat history: \n'.encode('utf-8'))
        client.send(history.encode('utf-8'))

        #send commands
        client.send('[Admin] To see commands please enter: !help \n'.encode('utf-8'))

        #start thread for handle_client
        thread = threading.Thread(target=handle_client, args = (client,nickname))
        thread.start()

#server start
print(f'[Admin] Server started... Searching for clients...')
receive()