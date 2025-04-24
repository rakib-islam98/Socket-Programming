import socket
import time

HOST = 'localhost'
PORT = 12346

messages = [
    "Hello",
    "How are you?",
    "This is message 3",
    "Final message"
]

client_socket = socket.socket()
client_socket.connect((HOST, PORT))
client_socket.settimeout(3)  

message_id = 0

while message_id < len(messages):
    message = messages[message_id]
    full_message = f"{message_id}:{message}"
    print(f"\nSender: Sending message {message_id} - \"{message}\"")
    client_socket.send(full_message.encode())

    try:
        ack = client_socket.recv(1024).decode()
        if ack == f"ACK:{message_id}":
            print(f"Sender: ACK received for message {message_id}")
            message_id += 1
        else:
            print(f"Sender: Unexpected ACK: {ack}. Resending...")
    except socket.timeout:
        print(f"Sender: Timeout! No ACK for message {message_id}. Resending...")

    time.sleep(1)

# End transmission
client_socket.send("END".encode())
client_socket.close()
