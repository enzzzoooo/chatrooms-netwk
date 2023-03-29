import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

client_socket.connect(localIP,localPort)

while True:
    sockets = [sys.stdin, client_socket]

    select.select()
    read_sockets, write_socket, error_socket = select.select(sockets,[],[])
 
    for socks in read_sockets:
        if socks == client_socket:
            message = socks.recvfrom(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            client_socket.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
client_socket.close()