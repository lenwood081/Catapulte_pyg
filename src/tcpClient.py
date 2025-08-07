import socket
import threading
import time

class TCPClient:
    def __init__(self):
        pass

    def connect(self, bind_ip='127.0.0.1', bind_port=9999):
        # create TCP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server
        client.connect((bind_ip, bind_port))

        # ----- AI ------
        message = "Hello from the client!"
        client.sendall(message.encode('utf-8'))

        data = client.recv(1024)  # Receive up to 1024 bytes
        print(f"Received from server: {data.decode('utf-8')}")


    def get_new_frame(self):
        """
        gets the most recent update frames sent from the server
        clears the update buffer, and returns these frames
        client should impliment the frames in the order recived 
        """
        pass
        

