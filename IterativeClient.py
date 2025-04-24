import socket

HOST = '127.0.0.1'
PORT = 12345

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(client.recv(1024).decode())  

    while True:
        message = input("You (client): ")
        client.send(message.encode())
        if message.lower() == 'exit':
            print("Disconnected from server.")
            break
        response = client.recv(1024).decode()
        print("Server:", response)

    client.close()

start_client()
