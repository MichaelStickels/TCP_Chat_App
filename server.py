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
def broadcast(user_message, sender):
    
    for client in client_list:
        if client != sender:
            client.sendall(user_message.encode(FORMAT))
        
#___________________________________________________________________________________________________________________________
#This function will receive and handle the messages that every client sends.
#It will broadcast the messages to every client
#Since this function will broadcast the messages continously, we want it 
#to run infinitely 
#The function takes in the client socket so that it can receive messages from
#that client.
#The fucntion tales in the client address so that it can send print out the 
#client's address in the chatroom

def client_handling(client_sock):

    username = client_sock.recv(4096).decode(FORMAT)

    broadcast(f"server|{str(username)} has joined the chat!") #Broadcasts a message telling everyone 
                                                     #who just connected to the server
   
    while True:
        #print('1')
        
        try:
            #print('2')
            message = client_sock.recv(4096).decode(FORMAT)
            print(message)
            #print('3')
            broadcast(message)
            #print('4')
        except: #If there is an error, then we should close and remove the socket
            print('9')
            client_list.remove(client_list.index(client_sock))
            client_sock.close()
            
#___________________________________________________________________________________________________________________________

#This function will create a socket for clients to bind to. Clients will pass in their IP address and port number
#and the fucntion will create a socket 
def server_init(IP, port):
    
    serv = socket(AF_INET, SOCK_STREAM) #Creating a socket
    serv.bind((IP, port)) #Binding the socket to the IP and Port number
    serv.listen() #Set server to listening mode to receive data from the client 

    return serv
#___________________________________________________________________________________________________________________________

if (len(sys.argv) < 2):
    print("Enter IP Address:" + sys.argv[0] + " and relay port:")
    sys.exit(1)
    
#assert(len(sys.argv) == 2)
IP = str(sys.argv[1])
port=int(sys.argv[2])


server = server_init(IP,port)

client_list=[];

while True: #This loop will continuously run as long as the client is connected 
        client_socket, address = server.accept() #accepts all connections and returns the client socket and address
        print(f"Connected with {str(address)}")
        client_list.append(client_socket)
        print(client_list)
        
        thread = threading.Thread(target=client_handling, args=(client_socket,)) #starts the threading 
        thread.start()


        if (client_socket.recv(4096).decode(FORMAT) == 'disconnect'):
            break
            
client_socket.close()
server.close()
