import socket

HOST = '127.0.0.1'
PORT = 12345

def start_iterative_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)  
    print(f"Iterative Server listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")
        client.send("You are connected to the server. Type 'exit' to disconnect.\n".encode())

        while True:
            try:
                message = client.recv(1024).decode()
                if message.lower() == 'exit':
                    print(f"Client {addr} disconnected.")
                    break
                print(f"{addr} : {message}")
                response = input("Server: ")
                client.send(response.encode())
            except:
                break

        client.close()

start_iterative_server()
