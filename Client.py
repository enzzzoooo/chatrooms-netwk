import socket
from time import sleep

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
#def helpcommands():
    # create help commands and descriptions
    # clear help commands once user has input a message/prompt

clientIP = "127.0.0.1"

clientPort = random.randint(8000, 10000)

bufferSize = 1024

client_socket.bind((clientIP, clientPort))

print("\nWelcome to chatroom of glorious nation of Kazakhstan!\n")
print("----- USER COMMANDS -----")
print("\nJOIN CHATROOM: /join <server_ip_add> <port>")
print("LEAVE CHATROOM: /leave")
print("REGISTER HANDLE: /register <handle>")
print("BROADCAST MESSAGE TO ALL: /all <message>")
print("SEND DIRECT MESSAGE TO SINGLE HANDLE: /msg <handle> <message>\n")

def receive():
    while True:
        try:
            message, address = client_socket.recvfrom(1024)
            print(message.decode())
        except:
            pass


receive_thread = threading.Thread(target=receive)
receive_thread.start()

user_registered = False
user_joined = False

user_input = input("\nEnter text here: ")

while True:
    if(user_input == "/leave" and user_registered == True and user_joined == True):
        print("\nConnection closed. Thank you!")
        client_socket.sendto(f"\n{name} has left the chatroom.".encode(), (serverIP, serverPort))
        serverIP, serverPort = 0
        break
    elif (user_input.startswith("/join")):
    # get local ip and port by doing a substring of the join command
        client_details = user_input.split()
        serverIP = client_details[1]
        serverPort = int(client_details[2])
        bufferSize = 1024
        print("\nConnection to the Message Board Server is successful!")
        client_socket.sendto(f"\nPort #{clientPort} has connected to the chatroom!".encode(), (serverIP, serverPort))
        user_joined = True
    elif(user_input.startswith("/register")):

        name = user_input.split()[1]
        client_socket.sendto(f"HANDLE:{name}".encode(), (serverIP, serverPort))
        user_registered = True

    elif(user_input.startswith("/msg") or user_input.startswith("/all") and user_registered == True):
        client_socket.sendto(f"\n{user_input} {clientPort}".encode(),(serverIP, serverPort))
        #client_socket.sendto(f"{name}: {sent_message}".encode(), (serverIP, serverPort))
    elif(user_input.startswith("/?")):
        print("----- USER COMMANDS -----")
        print("\nJOIN CHATROOM: /join <server_ip_add> <port>")
        print("LEAVE CHATROOM: /leave")
        print("REGISTER HANDLE: /register <handle>")
        print("BROADCAST MESSAGE TO ALL: /all <message>")
        print("SEND DIRECT MESSAGE TO SINGLE HANDLE: /msg <handle> <message>\n\n")
    else:
        print("\nCommand not found. Use /? for the command list.")

    user_input = input("\nEnter text here: ")

    sleep(0.75)









# fix register so that we comply with specs


# create mod code so that user can leave


