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

class Figure:

    def __init__(self, shape: str, color: str, x: int = 4, y: int = 0) -> None:
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

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
