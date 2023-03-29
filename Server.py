import socket
import select
import sys
import time

from _thread import *

print("hello")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
code to take localIP and port from args instead of declaring them:


if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")

localIP = str(sys.argv[1])

localPort = int(sys.argv[2])

"""

localIP     = "127.0.0.1"

localPort   = 8888

bufferSize  = 2048

server_socket.bind((localIP,localPort))

client_list = []


# functions
def broadcast(message, sender_socket):
    for client_socket in client_list:
        if client_socket != sender_socket:
            server_socket.sendto(message.encode(), client_address)

def client_thread(client_socket, client_address):
    broadcast("[" + time.ctime(time.time()) + "  " + client_address[0] +  "] : " + message.decode(), client_address)



while(True):
    message, client_address = server_socket.recvfrom(bufferSize)

    if client_address not in client_list:
        client_list.append(client_address)

    print (client_address[0] + " connected")

    start_new_thread(client_thread,(message, client_address))
