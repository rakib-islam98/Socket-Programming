import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
clients = []

def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client, addr):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            # Prefix message with the client address
            tagged_message = f"{addr[0]}:{addr[1]} says: {message.decode()}".encode()
            broadcast(tagged_message, client)
        except:
            break
    client.close()
    clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"New connection: {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
