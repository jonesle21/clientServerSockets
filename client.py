#Author: Laura Jones
#Date: 11/29/2021
#Class: CS 372 Fall 2021
#Assignment: Portfolio Project
#write a simple client-server chat program using python sockets. For extra-credit turn your chat program into a simple ascii multiplayer game 

import socket


#Citation for functions used:
#Adapted from 
#Source URL: https://docs.python.org/3/howto/sockets.html#using-a-socket


client_socket = socket.socket()
client_socket.connect(("localhost", 32451))

print("Type /q to quit")
print("Enter message to send...")
chat = input(">")
#sned intial hello statement
client_socket.send(chat.encode())

while True:
    #receive message from server and check if it says '/q' to quit
    message = client_socket.recv(2048).decode()
    #break loop if '/q'
    if message == "/q":
        break
    #print message from server
    print(message)
    #get input from client side and send to server
    chat = input(">")
    client_socket.send(chat.encode())
    #break loop if '/q'
    if chat == "/q":
        break

client_socket.close()
