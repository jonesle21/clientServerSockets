#Author: Laura Jones
#Date: 11/29/2021
#Class: CS 372 Fall 2021
#Assignment: Portfolio Project
#write a simple client-server chat program using python sockets. For extra-credit turn your chat program into a simple ascii multiplayer game 

import socket


#Citation for functions used:
#Adapted from 
#Source URL: https://docs.python.org/3/howto/sockets.html#using-a-socket
   
server_socket = socket.socket()  
# set a socket reuse option before the bind command on the server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# bind host address and port together
server_socket.bind(("localhost", 32451)) 
#listen for as many as 1 client request
server_socket.listen(1)
# accept new connection
(client_socket, address) = server_socket.accept() 


print("Connection from: " + str(address))
print('waiting for message ...')
chat = client_socket.recv(2048).decode()
print(str(chat))
print('Type /q to quit')
print("Enter message to send...") 


while True:
    message = input(">")
    #if we are going to send '/q' we break the loop and close the sockets
    if message == "/q":
        break
    client_socket.send(message.encode())  # send data to the client
    chat = client_socket.recv(2048).decode()
    #if we receive "/q" we break the loop and close the sockets
    if str(chat) == "/q":
        break
    print(str(chat))

client_socket.close()  # close the connection
server_socket.close()