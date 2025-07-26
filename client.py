import socket

# Step 1: Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# Step 3: Communication loop
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

# Step 4: Close socket
client_socket.close()
