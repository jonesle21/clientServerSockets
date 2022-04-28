# clientServerSockets

My files, client.py and server.py communicate with each other using the socket library in python.
Using the socket library in python, the client side uses s.connect() with the arguments localhost and the 
matching port number of the server side. Client side then sends initial message to server, enters while 
loop and continues to receive and send messages until either the client or the server sends ‘/q’. Then it 
closes the client socket. 

Using the socket library in python the server side uses s.setsockopt() to be able to resuse option and 
then uses s.bind() to bind the socket to localhost, at same port as client. Then it is set to listen to exactly 
1 client and accept the connection. It then waits to receive the initial message from the client and print 
it out. It then enter a while loop similar to the client side where it gets the servers message checks for 
the quit signal and waits for client message and checks for the quit signal. When either the client or the 
server sends the quit signal it breaks the loop and closes both client and server sockets. 

Here is the server side. It is run by using the command python server.py when in the same directory.

![image](https://user-images.githubusercontent.com/67295425/165821753-be33d345-5647-4a93-ac86-c31d8702b8aa.png)

Here is the client side. It is run by using the command python client.py when in the same directory.

![image](https://user-images.githubusercontent.com/67295425/165821829-4d92702a-5c12-40e8-b6d3-e096e34642cf.png)
