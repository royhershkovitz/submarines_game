from game1v1 import Game1v1
from UI.cli_ui import CLI_UI
from network.tcp_implementation import TCPImplementation
from game_protocol.octet_implementation import OctetImplementation
from game_protocol.octet_implementation import OctetImplementation
GAME_PORT = 25565
LOCALHOST = "localhost"


def main():
    game_network_protocol = OctetImplementation(TCPImplementation(LOCALHOST, GAME_PORT))
    game = Game1v1(CLI_UI(), game_network_protocol)
    game.start()

if __name__ == "__main__":
    main()
