"""
Purpose: network exceptions definition
Author: roy
Creation date: 29.12.2020
"""

class NetworkError(Exception):
    """
    error to create a message
    """
    def __init__(self, message):
        super().__init__(message)

class EXITError(Exception):
    """
    error to create a exit procedure
    """
    def __init__(self, message):
        super().__init__(message)
