######################################################################################################################################################
# Name: James A. Chase
# File: lib.py
# Date: 6 November 2023
# Description:
#
# File to hold static data, and other calculation functions for engine.py
#
######################################################################################################################################################

# imports
from typing import List
from figure import Figure

def get_shapes_arr() -> List[str]:
    '''
    Retrieves the valid shapes array.

    Parameters: None

    Returns:
        - a list containing the valid shapes for Tetris
    '''
    return ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

def update_board(board: List[List[int]], figure: Figure) -> None:
    '''
    Updates the internal game board to reflect the graphical representation.

    Parameters:
        - board: a 2-D list of integers representing the current board state
        - figure: a Figure object representing a Tetrimino.

    Returns: None
    '''
    for y, row in enumerate(figure.shape):
        for x, cell in enumerate(row):
            if cell: board[figure.y + y - 1][figure.x + x] = 1

def clear_completed_rows(board: List[List[int]], col: int) -> int:
    '''
    Clears completed rows from the board.

    Parameters:
        - board: a 2-D list of integers representing the current board state
        - col: an integer representing the in-game column count

    Returns:
        - an integer indicating how many rows were cleared.
    '''
    completed_rows = []

    for y, row in enumerate(board):
        if all(row): completed_rows.append(y)

    for y in completed_rows:
        del board[y]
        board.insert(0, [0] * col)
    
    return len(completed_rows)

def check_collision(board: List[List[int]], figure: Figure, rows: int) -> bool:
    '''
    Checks collision for the Tetrimino.

    Parameters:
        - board: a 2-D list of integers representing the current board state
        - figure: A Figure object representing a Tetrimino.
        - rows: an integer representing the in-game row count

    Returns:
        - a boolean value indicating if the Tetrimino has collided with something
    '''
    for y, row in enumerate(figure.shape):
        for x, cell in enumerate(row):
            if cell and (figure.y + y >= rows or board[figure.y + y][figure.x + x]): return True
    return False

def check_rotation(board: List[List[str]], figure: Figure, col: int, rows: int) -> bool:
    '''
    Checks to see if a rotation is possible for the current Figure.

    Parameters:
        - board: a 2-D list of integers representing the current board state
        - figure: a Figure object representing a Tetrimino.
        - col: an integer representing the in-game column count
        - rows: an integer representing the in-game row count

    Returns:
        - a boolean value indicating if the Tetrimino can rotate or not.
    '''
    for y, row in enumerate(figure.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x, new_y = figure.x + x, figure.y + y
                if (
                    new_x < 0
                    or new_x >= col
                    or new_y >= rows
                    or (new_y >= 0 and board[new_y][new_x])
                ): return False
    return True

def game_over(board: List[List[int]], figure: Figure) -> bool:
    '''
    Checks if the game is over.

    Parameters:
        - figure: A Figure object representing a Tetrimino.

    Returns:
        - a boolean value indicating if the game is over or not.
    '''
    for y, row in enumerate(figure.shape):
        for x, cell in enumerate(row):
            if cell:
                if figure.y + y < 0 or board[figure.y + y][figure.x + x]: return True
    return False

if __name__ == '__main__': assert False, "This is a module. Please import its contents into another file."
