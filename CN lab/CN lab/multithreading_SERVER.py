
import socket
import threading

# Function to handle each client
def handle_client(conn, addr):
    print(f"[+] New connection from {addr}")
    conn.send(b"Welcome to the Multi-threaded Server!\n")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode().strip()}")
            conn.send(b"Message received!\n")
        except:
            break

    print(f"[-] Connection closed from {addr}")
    conn.close()

# Main server code
def main():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[SERVER] Listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
# This code implements a multi-threaded TCP server that can handle multiple clients simultaneously.