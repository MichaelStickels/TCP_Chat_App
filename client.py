import sys
import os
import random
import string
import threading
import time
from socket import *

FORMAT = 'utf-8'
#____________________________________________________________________________________________________________________________________________________________________
# This fucntion does important and inspiring things 
# It works by magic squrriels 
# 
def connection_init():

    HOST = input("Enter chatroom IP: ")
    PORT = int(input("Enter chatroom port: "))
    print("...connecting...")

    #create socket and connect to ip and port
    s = socket(AF_INET, SOCK_STREAM)
    #s.connect((HOST, PORT))

    print("Connected to chatroom")
    
    username = str(input("Enter username: "))

    # send username to server
    #s.sendall(str.encode(username))

    print("Type 'disconnect' to exit chatroom")
    
    return(username)


#____________________________________________________________________________________________________________________________________________________________________
# This fucntion does important and inspiring things 
# It works by magic squrriels 
# 
def message_handling():
    while True:
        
        print('message_thread')
        time.sleep(10)
    



#____________________________________________________________________________________________________________________________________________________________________
# This fucntion does important and inspiring things 
# It works by magic squrriels 
# 
def input_handling():
    while True:
        
        inp = input("Message: ")
        if inp == 'disconnect':
            print("Disconnecting...")
            os._exit(1)
        else:
            #send message
            print("message sent")



# Run

# Initialize connection and take user input
username = connection_init()

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