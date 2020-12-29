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
    def check_coords_location(self, x, y)->int:
        """
        will get the board contents at x, y
        :param x:
        :param y:
        :return:    0 miss
                    1 ship
                    2 hit location
                    3 hit location + ship
        """
        pass
