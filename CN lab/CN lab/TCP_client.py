
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 12345

client_socket.connect((host,port))

data = client_socket.recv(1024)

print("Received form server : ",data.decode())

client_socket.close()
