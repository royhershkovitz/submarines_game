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
    def attack(self, x:int, y:int)->bytes:
        """
        will attack the opponent on the given coords
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
