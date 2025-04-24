import socket
import threading

# Server address
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            print("Connection lost.")
            break

def send_messages(sock):
    while True:
        try:
            message = input()
            sock.send(message.encode())
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connected to the chat server.")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    send_messages(client)

if __name__ == "__main__":
    start_client()
