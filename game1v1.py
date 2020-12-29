"""
Purpose: The game implementation as class
Author: roy
Creation date: 29.12.2020
"""

class Game1v1():
    """
    game 1v1 logic
    """
    def __init__(self, game_protocol, ui):
        self.game_protocol = game_protocol
        self.ui = ui
    
    def play_host(self):
        self.get_ships()
        self.play()

    def play_client(self):
        self.send_ships()
        self.play()

    def play(self):
        self.ui.put_ships()
        self.game_protocol.start()
