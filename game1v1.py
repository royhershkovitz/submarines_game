"""
Purpose: The game implementation as class
Author: roy
Creation date: 29.12.2020
"""
import collections
import logging
from board.board_implementation import Board
from game_protocol.network_exception import NetworkError, EXITError
SHIPS=[2,3,3,4,5]
MY_TURN = 0
OPPONENT_TURN = 1
BOARD_SIZE = 10
MISS = 1


class Game1v1():
    """
    game 1v1 logic
    """
    def __init__(self, ui, game_protocol):
        self.game_protocol = game_protocol
        self.ui = ui
        self.ships_sizes = SHIPS
        self.logger = logging.getLogger("Game1v1")
        self.make_result = collections.namedtuple("Result", "x y result")

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
        self.ui.message("Hosting!")
        self.game_protocol.start_host()        
        self.ships_sizes = self.game_protocol.get_ships()
        self.play(MY_TURN)

    def play_client(self):
        if not self.game_protocol.connect():
            self.ui.host_not_online()
            return
        self.game_protocol.send_ships(self.ships_sizes)
        self.play(OPPONENT_TURN)

    def play(self, turn):
        self.my_board = Board(BOARD_SIZE, BOARD_SIZE)
        ships_locations = self.ui.put_ships(self.ships_sizes)
        while not self.my_board.place_ships(ships_locations):
            ships_locations = self.ui.put_ships(self.ships_sizes)
        self.enemy_board = Board(BOARD_SIZE, BOARD_SIZE)
        self.game_protocol.start()
        while True:
            try:
                if turn == MY_TURN:
                    self.ui.update_turn("you")
                    point = self.ui.get_user_target()
                    response = self.game_protocol.attack(point)
                    self.enemy_board.update_location(response)
                    self.ui.update_enemy_board(response)
                    if value != MISS:
                        turn = OPPONENT_TURN
                elif turn == OPPONENT_TURN:
                    self.ui.update_turn("opponent")
                    point = self.game_protocol.wait_for_turn()
                    value = self.my_board.get_hit_result(point)
                    self.game_protocol.response_to_attacker(value)
                    self.ui.update_attacks(self.make_result(point.x, point.y, value))
                    if value != MISS:
                        turn = MY_TURN
                else:
                    self.logger.error("turns are broken")
                    break
            except (NetworkError, KeyboardInterrupt, EXITError) as e:
                self.logger.error(e)
                self.game_protocol.quit()
        self.logger.error("exit game")
