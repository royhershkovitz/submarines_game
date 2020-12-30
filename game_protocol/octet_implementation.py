"""
Purpose: interface implementation for the game communication logic
Author: roy
Creation date: 29.12.2020
"""
from abc import ABCMeta, abstractmethod
import collections
import logging
from game_protocol.network_exception import NetworkError, EXITError
#TOP_VALUE < 15 because \xFF is quit signal
TOP_VALUE = 14
START = b'\xFF'
QUIT = b'\xFF'


class OctetImplementation(metaclass=ABCMeta):
    """
    interface implementation for the game coomands and logic
    """
    def __init__(self, network_client):
        self.network_client = network_client
        self.logger = logging.getLogger("OctetImplementation")
        self.make_result = collections.namedtuple("Result", "x y result")
        self.make_point = collections.namedtuple("Point", "x y")

    def start_host(self):
        self.logger.debug(f"start host")
        self.network_client.listen()
    
    def connect(self):
        self.logger.debug(f"start client")
        try:
            self.network_client.connect()
        except (ConnectionResetError, ConnectionRefusedError) as e:
            self.logger.warn(e)
            return False
        return True

    def start(self):
        """
        will send a message to start the game and wait for the response
        """
        self.logger.info(f"send start byte")
        self.network_client.send(START)
        recv_bytes = self.network_client.recv()
        if recv_bytes and len(recv_bytes) > 0:
            start_byte = recv_bytes[0]
            return start_byte == START
        return False

    def send_ships(self, ships:list):
        """
        will send a message about the default size and boats
        :param ships: list of int represents ship sizes
        """
        message = [len(ships)]
        message.extend(ships)
        message = bytes(message)
        self.network_client.send(message)

    def get_ships(self):
        """
        will send a message to start the game and wait for the response
        """
        self.network_client.recv()
        return [2, 3, 3, 4, 5]

    def quit(self):
        """
        will send a quit message
        """
        self.logger.debug(f"quiting the game")
        self.network_client.send(QUIT)
        self.network_client.close()

    def attack(self, point)->bytes:
        """
        will attack the opponent on the given coords
        :param point:
            :param x: number < 16
            :param y: number < 16
        :return: the other client response
        """
        x, y = point
        if x > TOP_VALUE or x < 0 or y > TOP_VALUE or y < 0:
            raise NetworkError("The protocol does not support x,y coords outside [0,15]")
        attack_value = x
        attack_value += y<<4
        attack_value = bytes([attack_value])
        self.network_client.send(attack_value)
        result = self.network_client.recv()
        if result and len(result) > 0:
            result = result[0]
            if result==QUIT:
                raise EXITError("Opponent left")
        else:
            raise NetworkError("Opponent broke protocol in attack response")
        return self.make_result(x, y, result)

    def wait_for_turn(self):
        """
        will get what happened
        """
        recv_bytes = self.network_client.recv()
        if recv_bytes and len(recv_bytes) > 0:
            attack_value = recv_bytes[0]
            x = attack_value%16
            y = attack_value>>4
            return self.make_point(x,y)
        raise NetworkError("Opponent broke protocol in his turn")

    def response_to_attacker(self, response):
        """
        will send a response
        """
        response = bytes([response])
        self.network_client.send(response)
