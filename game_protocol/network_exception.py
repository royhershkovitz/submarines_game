"""
Purpose: network exceptions definition
Author: roy
Creation date: 29.12.2020
"""

class NetworkError(Exception):
    """
    error to create a message
    """
    def __init__(self, message, errors):
        super().__init__(message)
