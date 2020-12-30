"""
Purpose: interface for user interaction
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod


class UIInterface(metaclass=ABCMeta):
    """
    interface for the user interaction
    """
    @abstractmethod
    def put_ships(self, ships:list)->list:
        """
        will handle ships placing ui and return
        :ships: the available ships length, and suggested position
        :return: the ships location
        """
        pass
    @abstractmethod
    def get_user_target(self)->tuple:
        """
        will get the user next target
        :return: namedtuple of the coords
        """
        pass
    @abstractmethod
    def update_turn(self, name):
        """
        will setup the current turn
        """
        pass
    @abstractmethod
    def message(self, text:str):
        """
        will present a message to the user
        """
        pass
    @abstractmethod
    def host_not_online(self):
        """
        cannot connect to host
        """
        pass
    @abstractmethod
    def update_enemy_board(self, missile_result):
        """
        will update the attack result on board
        :param missile_result: named tuple containing who, x, y, result
        who - string name
        result - 0 miss
        result - 1 hit
        result - 2 sink
        """
        pass
    @abstractmethod
    def update_attacks(self, missile):
        """
        will update the attack result on out board
        :param missile: named tuple containing who, x, y, result
        who - string name
        """
        pass
#you won you lost?
#menu/ choose game mode/choose port ip
#host_not_online
