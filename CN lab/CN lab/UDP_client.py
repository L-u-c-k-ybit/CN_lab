
import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
host = 'localhost'
port = 57000

# Message to send
message = "Hello UDP Server!"
client_socket.sendto(message.encode(), (host, port))

# Receive response
data, server = client_socket.recvfrom(1024)
print("Received from server:", data.decode())

# Close socket
client_socket.close()
