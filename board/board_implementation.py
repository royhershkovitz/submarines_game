"""
Purpose: implementation for the game board logic
Author: roy
Creation date: 29.12.2020
"""
import numpy
from board.board_interface import BoardIntreface
START_BOARD = 1
INVALID = -1
MISS = 0
SHIP_POS = 1
HIT_LOC = 2

class Board(BoardIntreface):
    """
    implementation for the game board logic
    """
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = numpy.zeros((self.size_x, self.size_y), dtype=int)

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

    def set_hit_coords_location(self, x, y)->int:
        """
        will get the board contents at x, y
        will convert x,y coords from <1,n> to <0, n-1>
        :param x:
        :param y:
        :return:    0 miss
                    1 ship
                    2 hit location (already hitted)
                    3 hit location + ship
                    -1 not valid
        """
        #TODO add this code as @
        if point.x > self.size_x or point.x < START_BOARD:
            return INVALID
        if point.y > self.size_y or point.y < START_BOARD:
            return INVALID
        x-=1
        y-=1
        ret_value = self.board[x][y]
        self.board[x][y] |= HIT_LOC
        return ret_value
    
    def set_ship_coords_location(self, x, y):
        """
        will get the board contents at x, y
        will convert x,y coords from <1,n> to <0, n-1>
        will not set outside of bounds
        :param x:
        :param y:
        """
        if point.x > self.size_x or point.x < START_BOARD:
            return INVALID
        if point.y > self.size_y or point.y < START_BOARD:
            return INVALID
        x-=1
        y-=1
        self.board[x][y] |= (HIT_LOC|SHIP_POS)

    def place_ships(self, ships)->bool:
        """
        :param ships: list of named tuple ship-
            :param x:
            :param y:
            :param orientation: true vertical, false horizontal
            :param size:
        :return:    true if could fit the ship in this place
        """
        tmp_board = numpy.zeros((self.size_x, self.size_y), dtype=int)
        for ship in ships:
            if sum_submatrix(tmp_board, ship) > 0:
                return False
            if ship.orientation:
                for sub_y in range(ship.y, ship.y+ship.size):
                    tmp_board[ship.x][sub_y] = SHIP_POS
            else:
                for sub_x in range(ship.x, ship.x+ship.size):
                    tmp_board[sub_x][ship.y] = SHIP_POS
        self.board = tmp_board
        return True


def sum_submatrix(board, ship)->int:
    """
    :param board:
    :param ship: named tuple -
        :param x:
        :param y:
        :param orientation: true vertical, false horizontal
        :param size:
    :return: the sum of the area around the ship
    """
    area_sum = 0
    if ship.orientation:
        for sub_y in range(ship.y, ship.y + ship.size):
            area_sum += board[ship.x][sub_y]
    else:
        for sub_x in range(ship.x, ship.x + ship.size):
            area_sum += board[sub_x][ship.y]
    return area_sum
