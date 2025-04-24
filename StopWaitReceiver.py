import socket
import random
import time

HOST = 'localhost'
PORT = 12346

server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Receiver: Waiting for sender to connect...")
conn, addr = server_socket.accept()
print("Receiver: Connected to sender.")

expected_id = 0

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    if data == "END":
        print("Receiver: Transmission complete.")
        break

    message_id, message = data.split(":", 1)
    message_id = int(message_id)

    # Simulate message loss (30% chance)
    if random.random() < 0.3:
        print(f"Receiver: Message {message_id} LOST (no ACK sent).")
        continue

    if message_id == expected_id:
        print(f"Receiver: Received message {message_id} - \"{message}\"")
        time.sleep(1)
        conn.send(f"ACK:{message_id}".encode())
        expected_id += 1
    else:
        print(f"Receiver: Duplicate or out-of-order message {message_id}.")
        conn.send(f"ACK:{expected_id - 1}".encode())

conn.close()
server_socket.close()
