import queue
import socket
import select
import sys
import time
import threading
import re

print("hello ")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localIP = "127.0.0.1"

localPort = 12345

bufferSize = 1024

server_socket.bind((localIP, localPort))

client_list = [] # address and name
client_list_address = [] # address
message_queue = queue.Queue()


# receive messages
def receive():
    while True:
        try:
            message, client_address_source = server_socket.recvfrom(bufferSize)
            print(client_address_source, "says: ", message.decode())
            message_queue.put((message, client_address_source))
        except:
            print("you done fucked up")


# functions
def broadcast():
    while True:
        while not message_queue.empty():
            message, address = message_queue.get()
            print(message.decode)

            # register condition such that if register

            if message.decode().startswith("/join"):
                pass

            if message.decode().startswith("HANDLE:"):
                name = message.decode()[message.decode().index(":") + 1:]
                if name not in client_list:
                    client_list.extend([address, name])
                    client_list_address.append(address)

                    for client in client_list_address:
                        server_socket.sendto(f"\n{name} has joined the chatroom.".encode(), client)

                    server_socket.sendto(f"\nWelcome {name}!".encode(), address)
                else:
                    server_socket.sendto(f"\nError: Registration failed. Handle or alias already exists.".encode(), address)

            if address in client_list:
                if message.decode().startswith("/all"):
                    if len(message.decode()) >= 2:
                        # sent_message = re.sub('[/all]', "", message.decode())
                        for client in client_list_address:
                            server_socket.sendto(message, client)
                    else:
                        server_socket.sendto(f"\nError: Command parameters do not match or is not allowed.".encode(), address)

                if message.decode().startswith("/msg"):
                    if len(message.decode()) >= 3:

                        name = message.decode().split()[1]
                        sent_message = message.decode().split()[2:]
                        private_message = ""

                        for word in sent_message:
                            private_message += word + " "

                        if name in client_list:
                            destination_address = client_list[client_list.index(name)-1]
                            server_socket.sendto(f"{name}: {private_message}".encode(), destination_address)
                        else:
                            server_socket.sendto(f"\nError: Handle or alias not found.".encode(), address)
                    else:
                        server_socket.sendto(f"\nError: Command parameters do not match or is not allowed.".encode(), address)
                else:
                    server_socket.sendto(f"\nError: Command not found.".encode(), address)







            """

            for client in client_list_address:
                if message.decode().startswith("HANDLE:"):
                    # if client != address:
                    server_socket.sendto(f"{name} has joined the chatroom.".encode(), client)

                try:
                    if message.decode().startswith("/all"):
                        if len(message.decode()) == 2:
                            # sent_message = re.sub('[/all]', "", message.decode())
                            for client in client_list:
                                server_socket.sendto(message, client)
                        else:
                            server_socket.sendto(f"Error: Command parameters do not match or is not allowed.".encode(),
                                                 client)

                    if message.decode().startswith("/msg"):
                        if len(message.decode()) == 3:
                            sent_message = message.decode().split()[2:]
                            destination_address = message.decode().split().index(1)
                            if destination_address in client_list:
                                server_socket.sendto(sent_message, destination_address)
                        else:
                            server_socket.sendto(f"Error: Command parameters do not match or is not allowed.".encode(),
                                                 client)
                except:
                    print("you done fucked up")
                    server_socket.sendto(f"Error: Command not found.".encode(), client)

            """

receive_thread = threading.Thread(target=receive)
broadcast_thread = threading.Thread(target=broadcast)

receive_thread.start()
broadcast_thread.start()

