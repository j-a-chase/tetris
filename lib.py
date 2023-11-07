######################################################################################################################################################
# Name: James A. Chase
# File: lib.py
# Date: 6 November 2023
# Description:
#
# File to hold static data, and other calculations.
#
######################################################################################################################################################

# imports
from typing import Dict, List

def get_shapes() -> Dict[str, List[List[int]]]:
    '''
    Returns the 'shapes' dictionary containing the values of each shape

    Parameters: None

    Returns:
        - A dictionary containing the values of various shapes
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
    }

if __name__ == '__main__': assert False, "This is a module. Please import its contents into another file."
