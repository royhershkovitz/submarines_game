"""
Purpose: interface for user interaction
Author: roy
Creation date: 29.12.2020
"""
import collections
from UI.ui_interface import UIInterface
MISS = 0
HIT = 1
SINK = 2


class CLI_UI(UIInterface):
    """
    implementation for the user interaction
    """
    def __init__(self):
        self.make_ship = collections.namedtuple("Ship", "x y orientation size")
        self.make_point = collections.namedtuple("Point", "x y")
    
    def put_ships(self, ships:list)->list:
        """
        will handle ships placing ui and return
        :ships: the available ships length, and suggested position
        :return: the ships location
        """
        print(f"The ships sizes {ships}")
        ships_location = []
        for ship_size in ships:
            print(f"For ship {ship_size}")
            x = input("x: ")
            y = input("y: ")
            orientation = input("orientation: ")
            ships_location.append(self.make_ship(x, y, orientation, ship_size))
        return ships_location
    
    def get_user_target(self)->tuple:
        """
        will get the user next target
        :return: namedtuple of the coords
        """
        print(f"What is your target?")
        x = input("x: ")
        y = input("y: ")
        return make_point(x, y)
    
    def update_turn(self, name):
        """
        will setup the current turn
        """
        print(f"this is the turn of {name}")
    
    def message(self, text:str):
        """
        will present a message to the user
        """
        print(message)
    
    def update_enemy_board(self, missile):
        """
        will update the attack result on board
        :param missile: named tuple containing who, x, y, result
        who - string name
        """
        print(f"Attack on enemy at <{x},{y}> ", end="")
        print_result(missile.result)

    def update_attacks(self, missile):
        """
        will update the attack result on out board
        :param missile: named tuple containing who, x, y, result
        who - string name
        """
        self.update_enemy_board(missile)

def print_result(result):
    """
    will print the attack result
    :param missile: named tuple containing who, x, y, result
    who - string name
    result - 0 miss
    result - 1 hit
    result - 2 sink
    """
    if result == MISS:
        print("Miss.")
    if result == HIT:
        print("Hit!")
    if result == SINK:
        print("Sink!")
