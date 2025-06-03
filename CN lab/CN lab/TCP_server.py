
import socket;

# create a socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#initilize port and host

host = 'localhost'
port = 12345

#bind the port and host with server_socket

server_socket.bind((host,port))

#listen to client max 1 in a queue
server_socket.listen(1)
print("TCP server is waiting for client very much....")

conn,addr = server_socket.accept()
print(f"Connected to {addr}")

message = "Welcome to the TCP server noobs!"
conn.send(message.encode())

conn.close()
