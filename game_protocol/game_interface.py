"""
Purpose: interface for the game communication logic
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod


class GameIntreface(metaclass=ABCMeta):
    """
    interface for the game coomands and logic
    """
    @abstractmethod
    def start(self):
        """
        will send a message to start the game and wait for the response
        """
        pass
    @abstractmethod
    def start_host(self):
        """
        will start listen to requests
        """
        pass
    @abstractmethod
    def connect(self):
        """
        will connect to the host described in the network client
        """
        pass
    @abstractmethod
    def quit(self):
        """
        will send a quit message
        """
        pass
    @abstractmethod
    def response_to_attacker(self, response):
        """
        will send a response if needed
        """
        pass
    @abstractmethod
    def attack(self, point)->bytes:
        """
        will attack the opponent on the given coords
        :param point:
            :param x:
            :param y:
        :return: the other client response
        """
        pass
    @abstractmethod
    def wait_for_turn(self):
        """
        will get what happened in the competitor turn
        """
        pass
