"""
Purpose: interface implementation network communication
Author: roy
Creation date: 29.12.2020
"""
import socket
import logging
from network.stream_communicate_interface import StreamCommunicateIntreface


class TCPImplementation(StreamCommunicateIntreface):
    """
    tcp interface implementation for stream like communication
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.logger = logging.getLogger("TCPImplementation")

    def connect(self):
        """
        will connect to the other client values
        the server values given in the constructor
        """
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect((self.host, self.port))
        self.logger.info(f"client connected to {self.host, self.port}")

    def listen(self):
        """
        will listen to incoming connections 
        the server values given in the constructor
        """
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen(1)        
        (self.clientsocket, address) = self.serversocket.accept()
        self.logger.info(f"A client connected at {address} have connected to the server")

    def close(self):
        """
        will close-open connections
        """
        self.logger.debug(f"Closing the network")
        if self.serversocket:
            self.serversocket.close()
        if self.clientsocket:
            self.clientsocket.close()
        self.logger.debug(f"Network closed")

    def send(self, data:bytes):
        self.clientsocket.sendall(data)

    def recv(self)->bytes:
        self.logger.debug(f"blocking recv")
        return self.clientsocket.recv(1024)
