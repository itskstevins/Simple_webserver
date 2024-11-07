
import socket

# Set up server details
SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8000

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(1)

print(f"Server is listening on port {SERVER_PORT}...")

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()  # Get client request
    print(f"Received request:{request}")

    # Parse request to determine the requested file
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Default to index.html if no specific file is requested
    if filename == '/':
        filename = '/index.html'

    try:
        # Attempt to open and read the requested file
        with open('htdocs' + filename) as file:
            content = file.read()
            response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        # Return 404 error if file is not found
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    # Send the HTTP response
    client_connection.sendall(response.encode())
    client_connection.close()  # Close the connection
