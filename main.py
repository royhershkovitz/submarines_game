from game1v1 import Game1v1
from UI.cli_ui import CLI_UI
from network.tcp_implementation import TCPImplementation
from game_protocol.octet_implementation import OctetImplementation
from game_protocol.octet_implementation import OctetImplementation
GAME_PORT = 25565


def main():
    game_network_protocol = OctetImplementation(TCPImplementation("localhost", GAME_PORT))
    game = Game1v1(CLI_UI(), game_network_protocol)
    game.start()

if __name__ == "__main__":
    main()
