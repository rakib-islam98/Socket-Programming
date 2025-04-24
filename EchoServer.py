import socket
#create a socket object
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#define the host and port
host='0.0.0.0' #Localhost
port=3356       #port to bind

#bind the socket to the host and port
server_socket.bind((host,port))

#enable the server to listen for incoming connection (max 1 in the waiting queue)
server_socket.listen(1)
print("Server is listening on port",port)

#accept a client connection
client_socket,client_address=server_socket.accept()
print(f"Connection established with {client_address}")

#receive listen msg from client
while True:
    #receive data(max 1024 byte)
    data=client_socket.recv(1024).decode()
    if data.lower()=='exit':
        print("Closing connection with client")
        break
    print(f"Received from client: {data}")
    client_socket.send(data.encode())

#close the connection
client_socket.close()
server_socket.close()
