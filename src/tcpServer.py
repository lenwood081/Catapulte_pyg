import socket
import threading

class TCPServer:
    def __init__(self) -> None:
        self.bind_ip = '0.0.0.0' # all avalible interfaces
        self.bind_port = 9999

    def start(self):

        # create TCP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind socket to port
        server.bind((self.bind_ip, self.bind_port))

        # listen for connections (2)
        server.listen(2)

        print(f"[*] Listening on {self.bind_ip}:{self.bind_port}")

        # accept connection
        while True:
            client_socket, address = server.accept()

            # do something
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_handler.start()

    def handle_client(self, client_socket, address):
        print(f"Accepted connection from {address}")

    def send_all(self, message):
        # send to all clients
        pass


