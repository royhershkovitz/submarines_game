"""
Purpose: interface for the game board logic
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod


class BoardIntreface(metaclass=ABCMeta):
    """
    interface for the game board logic
    """
    @abstractmethod
    def update_location(self, missile_result):
        """
        will update the attack result on board
        will handle bounds check
        :param missile_result: named tuple containing who, x, y, result
        who - string name
        result - 0 miss
        result - 1 hit
        """
        pass
    @abstractmethod
    def get_hit_result(self, x, y)->int:
        """
        will get the board contents at x, y
        :param x:
        :param y:
        :return:    0 miss
                    1 ship
                    2 hit location
                    3 hit location + ship
                    -1 not valid
        """
        pass
    @abstractmethod
    def place_ships(self, ships)->bool:
        """
        :param ships: list of named tuple ship-
            :param x:
            :param y:
            :param size:
        :return:    true if could fit the ship in this place
        """
        pass    
    @abstractmethod
    def is_lost(self):
        """
        true if there are still active picese on the board
        """
        pass
