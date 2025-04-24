import socket
#create a socket object
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#define the host and port
host='192.168.0.107' #Localhost
port=3356       #port to bind

#bind the socket to the host and port
client_socket.connect((host,port))

#sends msg from client
while True:
    msg=input("Enter a message to send to the server(Type 'exit' to quit): ")
              
    #send data
    client_socket.send(msg.encode())
    
    #receive data(max 1024 byte)
    data=client_socket.recv(1024).decode()
    print(f"Received from server: {data}")
    
    if msg.lower()=='exit':
              break

#close the connection
client_socket.close()
