"""
Purpose: interface for user interaction
Author: roy
Creation date: 29.12.2020
"""
from UI.ui_interface import UIInterface


class CLI_UI(UIInterface):
    """
    interface for the user interaction
    """
    def put_ships(self, ships:list)->list:
        """
        will handle ships placing ui and return
        :ships: the available ships length, and suggested position
        :return: the ships location
        """
        print()
    def get_user_target(self)->tuple:
        """
        will get the user next target
        :return: namedtuple of the coords
        """
        pass
    def update_turn(self, name):
        """
        will setup the current turn
        """
        pass
    def message(self, text):
        """
        will present a message to the user
        """
        pass
    def update_enemy_board(self, missile_result):
        """
        will update the attack result on board
        :param missile_result: named tuple containing who, x, y, result
        who - string name
        result - 0 miss
        result - 1 hit
        """
        pass
