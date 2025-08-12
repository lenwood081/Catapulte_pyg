import socket
import threading
import time

# syntax
from tcpMessageSymbols import *

class TCPServer:
    def __init__(self) -> None:
        self.bind_ip = '0.0.0.0' # all avalible interfaces
        self.bind_port = 9997

        self.client_number = 0
        self.target_client_number = 2

        # client fram index array
        self.client_frame_index = [False for i in range(self.target_client_number)]

        # 2d array, client number and then array of frames 
        # frame array scafforlding
        self.frames = [[] for i in range(self.target_client_number)]

        self.all_connected = False

    def start(self):

        # create TCP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind socket to port
        server.bind((self.bind_ip, self.bind_port))

        # listen for connections
        server.listen(self.target_client_number)

        print(f"[*] Listening on {self.bind_ip}:{self.bind_port}")

        # accept connection
        while True:
            client_socket, address = server.accept()

            # do something
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address, self.select_free_client_number()))

            self.client_number += 1
            client_handler.start()

    def handle_client(self, client_socket, address, client_number):
        print(f"Accepted connection from {address}")
        self.all_connected = True

        # clear frame buffer
        # self.frames[client_number] = []
        while True:
            # send avalible frames until EOM recieved
            if self.frames[client_number]:
                # complile frame
                frame = SOF + self.frames[client_number][0] + EOF
                print(frame)

                # send frame
                client_socket.send(frame.encode())
                self.frames[client_number].pop(0)
            
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

        for i in range(self.target_client_number):
            # dont add to frame spots currently not in use
            if not self.client_frame_index[i]:
                continue

            self.frames[i].append(frame)
            print(self.frames[i])

    def clients_connected(self):
        return (self.target_client_number == self.client_number)

    def select_free_client_number(self):
        for i in range(self.target_client_number):
            if not self.client_frame_index[i]:
                # mark frame index as taken and return it
                self.client_frame_index[i] = True
                return i

        return -1

server = TCPServer()
server_thread = threading.Thread(target=server.start)

server_thread.start()

time.sleep(5)

server.add_frame("hello")


