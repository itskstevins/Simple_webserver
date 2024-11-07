import socket

def server():
   host = socket.gethostname()

   #specify the port to listen on
   port = 21042

   # create a socket object
   s = socket.socket()

   #Bind the socket to the host and port
   s.bind((host, port))

   # listen for incoming connection, allowing up to 2 clients
   s.listen(2)

   # accept incoming connection
   c, address = s.accept()

   while True:
       # Receive data from the client (up to 1024 bytes) and decode it
       data = c.recv(1024).decode()

       # If no data is received, break the loop
       if not data:
           break
       print(f"Received from client: {data}")

       # Get user input and send it to the client after encoding
       response = input("Enter response to send to client: ")
       c.send(response.encode())
    # Close the client connection
   c.close()

if __name__ == "__main__":
    # Start the server
    server()