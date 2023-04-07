import socket
import select
import sys
import threading
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
code to take localIP and port from args instead of declaring them:


if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")

localIP = str(sys.argv[1])

localPort = int(sys.argv[2])

"""

# codeblock here for help commands
def helpcommands():
    print("Welcome to chatroom of make benefit glorious nation of Kazakhstan!")

localIP = "127.0.0.1"

bufferSize = 1024

client_socket.bind((localIP, random.randint(8000, 10000)))

name = input("Nickname: ")

# put here codeblocks for join
def receive():
    while True:
        try:
            message, address = client_socket.recvfrom(1024)
            print(message.decode())
        except:
            pass


receive_thread = threading.Thread(target=receive)
receive_thread.start()
# fix register so that we comply with specs
client_socket.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 9005))

while True:
    sent_message = input("")
    # create mod code so that user can leave
    if sent_message == "/leave":
        exit()
    else:
        client_socket.sendto(f"{name}: {sent_message}".encode(), ("localhost", 9005))

# create mod code so that user can leave
vclient_socket.close()

