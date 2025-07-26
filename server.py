import socket

# Step 1: Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to host and port
host = '127.0.0.1'  # localhost
port = 12345
server_socket.bind((host, port))

# Step 3: Listen for connections
server_socket.listen()

print(f"Server is listening on {host}:{port}...")

# Step 4: Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected with {addr}")

# Step 5: Communication loop
while True:
    message = conn.recv(1024).decode()
    if not message:
        break
    print("Client:", message)
    reply = input("You: ")
    conn.send(reply.encode())

# Step 6: Close connection
conn.close()
