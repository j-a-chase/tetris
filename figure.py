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
from typing import Tuple, List

def get_shape(shape: str) -> List[List[int]]:
    '''
    Returns the values associated with the given shape.

    Parameters:
        - shape: a string containing the desired shape.

    Returns:
        - A 2-D List containing the values of the given shape.
    '''
    return {
        'I': [[1,1,1,1]],
        'J': [
            [0,0,1],
            [1,1,1]
        ],
        'L': [
            [1,0,0],
            [1,1,1]
        ],
        'O': [
            [1,1],
            [1,1]
        ],
        'S': [
            [0,1,1],
            [1,1,0]
        ],
        'T': [
            [0,1,0],
            [1,1,1]
        ],
        'Z': [
            [1,1,0],
            [0,1,1]
        ]
    }[shape]

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
    
    def rotate(self) -> List[List[int]]:
        '''
        Rotates the figure.

        Parameters: None

        Returns:
            - A 2-D list containing the rotated figure.
        '''
        self.shape = list(zip(*self.shape[::-1]))

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
