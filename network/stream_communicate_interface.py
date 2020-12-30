"""
Purpose: interface for network communication
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod


class StreamCommunicateIntreface(metaclass=ABCMeta):
    """
    interface for stream like communication
    """
    @abstractmethod
    def connect(self):
        """
        will connect to the other client values
        the server values given in the constructor
        """
        pass
    @abstractmethod
    def close(self):
        """
        will close-open connections
        """
        pass
    @abstractmethod
    def listen(self):
        """
        will listen to incoming connections 
        the server values given in the constructor
        """
        pass
    @abstractmethod
    def send(self, data:bytes):
        pass
    @abstractmethod
    def recv(self)->bytes:
        pass
