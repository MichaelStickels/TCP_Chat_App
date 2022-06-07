import sys
import os
import random
import string
import threading
from socket import *

FORMAT = 'utf-8'

#___________________________________________________________________________________________________________________________
#This fucntion will be used to broadcast a client's message to everyone. 
#It works by taking in the user message and sending the message to one at 
#a time to every client in the room
def broadcast(user_message):
    
    for client in client_list:
        client.send(user_message.encode(FORMAT))
        
#___________________________________________________________________________________________________________________________
#This function will receive and handle the messages that every client sends.
#It will broadcast the messages to every client
#Since this function will broadcast the messages continously, we want it 
#to run infinitely 
#The function takes in the client socket so that it can receive messages from
#that client.
#The fucntion tales in the client address so that it can send print out the 
#client's address in the chatroom

def client_handling(client_socket):
   
    while True:
        
        try:
            message = client_socket.recv(4096).decode(FORMAT)
            broadcast(message)
        except: #If there is an error, then we should close and remove the socket
            client_list.remove(client_list.index(client_socket))
            client_socket.close()
            
#___________________________________________________________________________________________________________________________

#This function will create a socket for clients to bind to. Clients will pass in their IP address and port number
#and the fucntion will create a socket 
def server_init(IP, port):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a socket
    server.bind((IP, port)) #Binding the socket to the IP and Port number
    server.listen() #Set server to listening mode to receive data from the client 
#___________________________________________________________________________________________________________________________

if (len(sys.argv) < 2):
    print("Enter IP Address:" + sys.argv[0] + " and relay port:")
    sys.exit(1)
    
#assert(len(sys.argv) == 2)
port=int(sys.argv[1])
IP = str(sys.argv[0])

server_init(IP,port)

client_list=[];

while True: #This loop will continuously run as long as the client is connected 
        client_socket, address = server.accept() #accepts all connections and returns the client socket and address
        print(f"Connected with {str(address)}")
        client_list.append(client_socket)
        
        
        broadcast(f"{str(client_socket)} has joined the chat!") #Broadcasts a message telling everyone 
                                                         #who just connected to the server
        
        thread = threading.Thread(target=client_handle, args=(client_socket,)) #starts the threading 
        thread.start()


        if (str(client_socket.recv(4096).decode(FORMAT)) == 'disconnect'):
            break
            
client_socket.close()
server.close()
