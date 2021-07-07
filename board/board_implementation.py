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
HIT_POS = 2
MISS_PROTOCOL = 1
HIT_PROTOCOL  = 2
SINK_PROTOCOL = 3

def check_bounds(function):
    def decorated_function(self, point):
        if point.x > self.size_x or point.x < START_BOARD:
            return INVALID
        if point.y > self.size_y or point.y < START_BOARD:
            return INVALID
        return function(self, point)
    return decorated_function

class Board(BoardIntreface):
    """
    implementation for the game board logic
    """
    def __init__(self, size_x, size_y, pieces):
        self.size_x = size_x
        self.size_y = size_y
        self.pieces = pieces
        self.board = numpy.zeros((self.size_x, self.size_y), dtype=int)

    @check_bounds
    def update_location(self, missile_result):
        """
        will update the attack result on board
        will handle bounds check
        will convert x,y coords from <1,n> to <0, n-1>
        :param missile_result: named tuple containing who, x, y, result
        who - string name
        result - 1 miss
        result - 2 hit
        result - 2 sink
        """
        self.board[missile_result.x-1][missile_result.y-1] |= HIT_POS
        if missile_result.result != MISS_PROTOCOL:
            self.board[missile_result.x-1][missile_result.y-1] |= SHIP_POS
        if missile_result.result == SINK_PROTOCOL:
            self.pieces -= 1

    @check_bounds
    def get_hit_result(self, point)->int:
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
        x = point.x - 1
        y = point.y - 1
        ret_value = self.board[x][y]
        self.board[x][y] |= HIT_POS
        if ret_value == SHIP_POS:
            if self._check_ship(x,y):
                self.pieces -= 1
                return SINK_PROTOCOL
            return HIT_PROTOCOL
        return MISS_PROTOCOL

    def _check_ship(self, x, y):
        """
        x,y in 0-n-1 coords
        """
        for tmp_x in range(x, self.size_x):
            if self.board[tmp_x][y] == SHIP_POS:
                return False
            elif self.board[tmp_x][y]&SHIP_POS == 0:
                continue
        for tmp_x in range(x-1,-1,-1):
            if self.board[tmp_x][y] == SHIP_POS:
                return False
            elif self.board[tmp_x][y]&SHIP_POS == 0:
                continue
        for tmp_y in range(y, self.size_y):
            if self.board[x][tmp_y] == SHIP_POS:
                return False
            elif self.board[x][tmp_y]&SHIP_POS == 0:
                continue
        for tmp_y in range(y-1,-1,-1):
            if self.board[x][tmp_y] == SHIP_POS:
                return False
            elif self.board[x][tmp_y]&SHIP_POS == 0:
                continue
        return True

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
        self.pieces = len(ships)
        return True

    def is_lost(self):
        """
        true if there are still active picese on the board
        """
        return self.pieces == 0


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
