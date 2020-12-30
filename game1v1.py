"""
Purpose: The game implementation as class
Author: roy
Creation date: 29.12.2020
"""
from board.board_implementation import Board
SHIPS=[2,3,3,4,5]
MY_TURN = 0
MY_TURN = 1
BOARD_SIZE = 10


class Game1v1():
    """
    game 1v1 logic
    """
    def __init__(self, game_protocol, ui):
        self.game_protocol = game_protocol
        self.ui = ui
        self.ships_sizes = SHIPS

    def start(self):
        print("Welcome to submarines game! choose mode: HOST|CLIENT")
        while True:
            what = input()
            if what == "HOST":
                self.play_host()
            elif what == "CLIENT": 
                self.play_client()
            else:
                print("no such option")

    def play_host(self):
        self.ships_sizes = self.game_protocol.get_ships()
        self.play(MY_TURN)

    def play_client(self):
        self.game_protocol.send_ships(self.ships_sizes)
        self.play(OPPONENT_TURN)

    def play(self, turn):
        self.my_board = Board(BOARD_SIZE, BOARD_SIZE)
        ships_locations = self.ui.put_ships(self.ships_sizes)
        while self.my_board:
            ships_locations = self.ui.put_ships(self.ships_sizes)
        self.enemy_board = Board(BOARD_SIZE, BOARD_SIZE)
        self.game_protocol.start()
        while True:
            if turn == MY_TURN:
                self.get_user_target()
                turn = OPPONENT_TURN
            elif turn == OPPONENT_TURN:
                self.wait_for_turn()
                turn = MY_TURN
            else:
                break
