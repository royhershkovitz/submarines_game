"""
Purpose: interface implementation for the game communication logic
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod
from game_protocol.network_exception import NetworkError

class OctetImplementation(metaclass=ABCMeta):
    """
    interface implementation for the game coomands and logic
    """
    def __init__(self, network_client):
        self.network_client = network_client
        self.logger = logging.getLogger('OctetImplementation')

    def start(self):
        """
        will send a message to start the game and wait for the response
        """
        self.logger.info(f"send start byte")
        self.network_client.send(b'\xff')
        recv_bytes = self.network_client.recv()
        if recv_bytes and len(recv_bytes) > 0:
            start_byte = recv_bytes[0]
            return start_byte == b'\xff'
        return False

    def send_ships(self):
        """
        will send a message about the default size and boats
        """
        self.network_client.send(b'\x05\x02\x03\x03\x04\x05')

    def get_ships(self):
        """
        will send a message to start the game and wait for the response
        """
        self.network_client.recv()
        return [2, 3, 3, 4, 5]

    def attack(self, x:int, y:int)->bytes:
        """
        will attack the opponent on the given coords
        :param x: number < 16
        :param y: number < 16
        :return: the other client response
        """
        if x > 15 or x < 0 or y > 15 or y < 0:
            raise NetworkError("The protocol does not support x,y coords outside [0,15]")
        attack_value = x
        y = y<<4
        attack_value += y
        attack_value = bytes([attack_value])
        self.network_client.send(attack_value)

    def wait_for_turn(self):
        """
        will get what happened
        """
        recv_bytes = self.network_client.recv()
        if recv_bytes and len(recv_bytes) > 0:
            attack_value = recv_bytes[0]
            x = attack_value%16
            y = attack_value>>4
            return (x,y)
        return None
