######################################################################################################################################################
# Name: James A. Chase
# File: figure.py
# Date: 6 November 2023
# Description:
#
# Class file for the Figure class. Represents a Tetris piece (Tetrimino).
#
######################################################################################################################################################

# imports
from lib import get_shape
from typing import Tuple

class Figure:
    def __init__(self, shape: str, color: Tuple[int, int, int], x: int = 3, y: int = 0) -> None:
        '''
        Constructor

        Parameters: None

        Returns: None
        '''
        # get the specified shape
        self.shape = get_shape(shape)

        # set the color
        self.color = color

        # set default x, y coordinate values
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int) -> None:
        '''
        Moves the figure the given amount.

        Parameters:
            - dx: an integer indicating how far to move the figure in the 'x' direction
            - dy: an integer indicating how far to move the figure in the 'y' direction

        Returns: None
        '''
        self.x += dx
        self.y += dy

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
