import socket
import threading
import time

# syntax
from tcpMessageSymbols import *

class TCPServer:
    def __init__(self) -> None:
        self.bind_ip = '0.0.0.0' # all avalible interfaces
        self.bind_port = 9999

        # 2d array, client number and then array of frames 
        self.frames = []

        self.client_number = 0
        self.target_client_number = 2

        self.all_connected = False

    def start(self):

        # create TCP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind socket to port
        server.bind((self.bind_ip, self.bind_port))

        # listen for connections
        server.listen(self.target_client_number)

        print(f"[*] Listening on {self.bind_ip}:{self.bind_port}")

        # accept connection
        while True:
            client_socket, address = server.accept()

            # do something
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address, self.client_number))

            self.client_number += 1
            client_handler.start()

    def handle_client(self, client_socket, address, client_number):
        print(f"Accepted connection from {address}")
        self.all_connected = True

        # create frame entry
        self.frames.append([])
        while True:
            # send avalible frames until EOM recieved
            if self.frames[client_number][0]:
                # send frame
                # break when EOM recieved
                pass
            
            if not self.all_connected:
                # send opposing player disconnected message
                break

        # some kind of indicator that disconnects all clients 
        self.all_connected = False

        print(f"Closing connection from {address}")
        client_socket.close()
        self.client_number -= 1

    def add_frame(self, frame):
        # if there are too many frames in one clients frame buffer
        # potentually wait/ lag server until they send through
        # or "combine" frame information for less frequent frame sending

        for client in self.frames:
            client.append(frame)

    def clients_connected(self):
        return (self.target_client_number == self.client_number)

server = TCPServer()
server.start()

