import sys
import os
import random
import string
import threading
from socket import *

FORMAT = 'utf-8'
#____________________________________________________________________________________________________________________________________________________________________
#This fucntion will be used to broadcast a client's message to everyone. 
#It works by taking in the user message and sending the message to one at 
#a time to every client in the room
def broadcast(user_message):
    
    for client in client_list:
        client.send(message)
        
#____________________________________________________________________________________________________________________________________________________________________
#This function will receive and handle the messages that every client sends.
#It will broadcast the messages to every client
#Since this function will broadcast the messages continously, we want it 
#to run infinitely 
def client_handling(client_socket, client_address):
    status = True
    while(status == True):
        message = client_socket.recv(2000)
        new_message = 
        broadcast(message)
        
#____________________________________________________________________________________________________________________________________________________________________
#This function will create a socket for clients to bind to. Clients will pass in their IP address and port number
#and the fucntion will create a socket 
def server_init(IP, port):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a socket

    server.bind((IP, port)) #Binding the socket to the IP and Port number

    server.listen() #Set server to listening mode to receive data from the client 

#____________________________________________________________________________________________________________________________________________________________________
if (len(sys.argv) < 2):
    print("Enter IP Address:" + sys.argv[0] + " and relay port:")
    sys.exit(1)
assert(len(sys.argv) == 2)
port=int(sys.argv[1])
IP = str(sys.argv[0])

server_init(IP,port)

client_list=[];
