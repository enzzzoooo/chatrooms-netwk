import queue
import socket
import select
import sys
import time
import threading

print("hello ")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
code to take localIP and port from args instead of declaring them:


if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")

localIP = str(sys.argv[1])

localPort = int(sys.argv[2])

"""

localIP = "127.0.0.1"

localPort = 9006

bufferSize = 1024

server_socket.bind((localIP, localPort))

client_list = []
message_queue = queue.Queue()

# receive messages
def receive():
    while True:
        try:
            message, client_address_source = server_socket.recvfrom(bufferSize)
            print(client_address_source, "says: ", message.decode())
            message_queue.put((message, client_address_source))
        except:
            pass


# functions
def broadcast():
    while True:
        while not message_queue.empty():
            message, address = message_queue.get()
            print(message.decode)
            if address not in client_list:
                    client_list.append(address)
            for client in client_list:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":")+1:]
                        server_socket.sendto(f"{name} has joined the chatroom!".encode(), client)
                    else:
                        server_socket.sendto(message, client)
                except:
                    client_list.remove(client)

receive_thread = threading.Thread(target=receive)
broadcast_thread = threading.Thread(target=broadcast)

receive_thread.start()
broadcast_thread.start()
