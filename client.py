import sys
import os
import threading
from socket import *

FORMAT = 'utf-8'
#____________________________________________________________________________________________________________________________________________________________________
# Initializes the socket and takes user input for server info and username
# 
def connection_init():

    HOST = input("Enter chatroom IP: ")
    PORT = int(input("Enter chatroom port: "))
    print("...connecting...")

    #create socket and connect to ip and port
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    print("Connected to chatroom")
    
    username = str(input("Enter username: "))

    # send username to server
    s.sendall(str.encode(username))

    print("Type 'disconnect' to exit chatroom")
    
    return(username, s)


#____________________________________________________________________________________________________________________________________________________________________
# Receives messages from the server and prints to the console
# 
def message_handling():
    while True:
        
        # Receive messages from the server
        # Messages are expected to be in the following format:
        # [username]|[message]
        data = sock.recv(4096).decode(FORMAT)

        user, message = data.split('|')

        print(user, ": ", message, sep='')
    



#____________________________________________________________________________________________________________________________________________________________________
# Takes input from the console and sends to the server
# Adds disconnect functionality and informs the server
def input_handling():
    while True:
        
        inp = input("Message: ")
        if inp == 'disconnect':
            print("Disconnecting...")
            sock.sendall(str.encode((str(username)+'|disconnected')))
            os._exit(1)
        else:
            #send message
            sock.sendall(str.encode((str(username)+'|'+str(inp))))
            # print(str.encode((str(username)+'|'+str(inp))))
            print("message sent")



# Run

# Initialize connection and take user input
global sock
username, sock = connection_init()

# Start a thread for incoming messages
message_thread = threading.Thread(target=message_handling)
message_thread.daemon = True
message_thread.start()

# Start a thread for input and outgoing messages
input_thread = threading.Thread(target=input_handling)
input_thread.daemon = True
input_thread.start()






# The compiler will be mad without this
exit = False
while True:
    if exit == True:
        sys.exit()