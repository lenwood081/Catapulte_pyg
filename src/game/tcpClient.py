import socket
import threading
import time

from tcpMessageSymbols import *

class TCPClient:
    def __init__(self):

        self.frame_buffer = []

        self.active_connection = False

    def connect(self, bind_ip='127.0.0.1', bind_port=9997):
        # create TCP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server
        client.connect((bind_ip, bind_port))
        self.active_connection = True

        # revieve frames
        message_buffer = ""
        while True:
            time.sleep(0.0001) # PERFORMANCE

            if not self.active_connection:
                break

            # use message buffer to piece together frames
            # save frame and clear buffer, SOF, EOF
            frame = client.recv(2048)
            message_buffer += frame.decode()
            if not message_buffer:
                continue

            frame_end = message_buffer.find(EOF)
            if frame_end != -1:
                frame_end += len(EOF)
                self.frame_buffer.append(message_buffer[:frame_end])
                message_buffer = message_buffer[frame_end:]


        client.close()

    def get_new_frame(self):
        """
        gets the most recent update frames sent from the server
        clears the update buffer, and returns these frames
        client should impliment the frames in the order recived 
        """
        if not self.frame_buffer:
            return

        frame = self.frame_buffer[0] 
        self.frame_buffer.pop(0)
        return frame

    def start_connection_thread(self):
        connection_handle = threading.Thread(target=self.connect)
        connection_handle.start()

    def stop_connection(self):
        self.active_connection = False

"""
client1 = TCPClient()
client1.start_connection_thread()

while True:
    time.sleep(0.01) # PERFORMANCE

    frame = client1.get_new_frame()
    if frame:
        print(frame)
"""
