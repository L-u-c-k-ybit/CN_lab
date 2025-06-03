import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define server address and port
host = 'localhost'
port = 57000

# Bind the socket to the address
server_socket.bind((host, port))
print("UDP server is up and listening on port", port)

# Server runs continuously
while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)
    print(f"Received from", {addr}, ":", data.decode())

    # Send a reply back to client
    server_socket.sendto(b"Hello from UDP Server!", addr)
    print("Reply sent to", addr)