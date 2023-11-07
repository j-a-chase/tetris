######################################################################################################################################################
# Name: James A. Chase
# File: engine.py
# Date: 6 November 2023
# Description:
#
# Class file for Engine class. Handles pygame assets and graphical generation.
#
######################################################################################################################################################

# imports
import pygame
from pygame import display
from figure import Figure
from random import choice

class Engine:
    def __init__(self, width: int = 1000, height: int = 800, columns: int = 10, rows: int = 20, size: int = 30) -> None:
        '''
        Constructor

        Parameters:
            - width: an integer representing the display width
            - height: an integer representing the display height
            - columns: an integer indicating how many columns the game will have
            - rows: an integer indicating how many rows the game will have
            - size: an integer indicating how big the grid should appear

        Returns: None
        '''
        # initialize pygame assets
        pygame.init()

        # define game colors
        self.BG_COLOR = (255, 255, 255)
        self.LINE_COLOR = (0, 0, 0)
        self.TEST_SHAPE_COLOR = (66, 233, 245)

        # set window values
        self.w = width
        self.h = height
        self.window = display.set_mode((width, height))
        display.set_caption("Tetris Clone")

        # set game values
        self.COLUMNS = columns
        self.ROWS = rows
        self.GRID_SIZE = size
        self.GRID_OFFSET_X = 200
        self.GRID_OFFSET_Y = 50

        self.move_delay = 400

        self.shapes_arr = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

        # define internal representation of game board
        self.board = [[0] * columns for _ in range(rows)]

        # run game
        self.run_game()

    def draw_grid(self) -> None:
        '''
        Draw game grid.

        Parameters: None

        Returns: None
        '''
        # draw tetriminos currently on board
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.window, self.TEST_SHAPE_COLOR,
                                     (self.GRID_OFFSET_X + x * self.GRID_SIZE, self.GRID_OFFSET_Y + y * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

        # draw board (allows lines to appear over the tetriminos)
        for y in range(self.ROWS):
            for x in range(self.COLUMNS):
                pygame.draw.rect(self.window,
                                 self.LINE_COLOR,
                                 (self.GRID_OFFSET_X + x * self.GRID_SIZE, self.GRID_OFFSET_Y + y * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE),
                                 1)
                
    def draw_figure(self, figure: Figure) -> None:
        '''
        Draws the given figure on the screen.

        Parameters:
            - figure: A Figure object that represents a Tetrimino.

        Returns: None
        '''
        for y, row in enumerate(figure.shape):
            for x, cell in enumerate(row):
                if cell: pygame.draw.rect(self.window, figure.color, 
                                          (self.GRID_OFFSET_X + figure.x * self.GRID_SIZE + x * self.GRID_SIZE,
                                           self.GRID_OFFSET_Y + figure.y * self.GRID_SIZE + y * self.GRID_SIZE,
                                           self.GRID_SIZE,
                                           self.GRID_SIZE))
                    
    def update_board(self, figure: Figure) -> None:
        '''
        Updates the internal game board to reflect the graphical representation.

        Parameters:
            - figure: a Figure object representing a Tetrimino.

        Returns: None
        '''
        for y, row in enumerate(figure.shape):
            for x, cell in enumerate(row):
                if cell: self.board[figure.y + y - 1][figure.x + x] = 1

    def clear_completed_rows(self) -> int:
        '''
        Clears completed rows from the board.

        Parameters: None

        Returns:
            - an integer indicating how many rows were cleared.
        '''
        completed_rows = []

        for y, row in enumerate(self.board):
            if all(row): completed_rows.append(y)

        for y in completed_rows:
            del self.board[y]
            self.board.insert(0, [0] * self.COLUMNS)
        
        return len(completed_rows)
                    
    def check_collision(self, figure: Figure) -> bool:
        '''
        Checks collision for the Tetrimino.

        Parameters:
            - figure: A Figure object representing a Tetrimino.

        Returns:
            - a boolean value indicating if the Tetrimino has collided with something
        '''
        for y, row in enumerate(figure.shape):
            for x, cell in enumerate(row):
                if cell and (figure.y + y >= self.ROWS or self.board[figure.y + y][figure.x + x]): return True
        return False
    
    def check_rotation(self, figure: Figure) -> bool:
        '''
        Checks to see if a rotation is possible for the current Figure.

        Parameters:
            - figure: a Figure object representing a Tetrimino.

        Returns:
            - a boolean value indicating if the Tetrimino can rotate or not.
        '''
        new_shape = [[0] * len(figure.shape[0]) for _ in range(len(figure.shape))]
        for y, row in enumerate(figure.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = figure.x + x, figure.y + y
                    if (
                        new_x < 0
                        or new_x >= self.COLUMNS
                        or new_y >= self.ROWS
                        or (new_y >= 0 and self.board[new_y][new_x])
                    ): return False
        return True
    
    def game_over(self, figure: Figure) -> bool:
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
                    if figure.y + y < 0 or self.board[figure.y + y][figure.x + x]: return True
        return False

    def run_game(self) -> None:
        '''
        Runs the main game loop.

        Parameters: None

        Returns: None
        '''
        self.window.fill(self.BG_COLOR)
        self.draw_grid()
        display.update()

        tetrimino = Figure('I', self.TEST_SHAPE_COLOR)
        move_timer = 0
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit(0)

                    if event.key == pygame.K_RIGHT:
                        if tetrimino.x < 10 - len(tetrimino.shape[0]): tetrimino.move(1,0)

                    if event.key == pygame.K_LEFT:
                        if tetrimino.x > 0: tetrimino.move(-1, 0)
                    
                    if event.key == pygame.K_DOWN:
                        while not self.check_collision(tetrimino): tetrimino.move(0, 1)

                    if event.key == pygame.K_r:
                        rotated = Figure('I', tetrimino.color, tetrimino.x, tetrimino.y)
                        rotated.shape = tetrimino.rotate()
                        if self.check_rotation(rotated):
                            tetrimino = rotated

            move_timer += 1
            if move_timer >= self.move_delay:
                tetrimino.move(0, 1)
                move_timer = 0

            if self.check_collision(tetrimino):
                self.update_board(tetrimino)
                tetrimino = Figure(choice(self.shapes_arr), self.TEST_SHAPE_COLOR)

                clear_count = self.clear_completed_rows()
                if clear_count > 0: print(f'{clear_count} rows cleared.')

                if self.game_over(tetrimino):
                    print('GAME OVER')
                    pygame.quit()
                    exit(0)

            self.window.fill(self.BG_COLOR)
            self.draw_figure(tetrimino)
            self.draw_grid()
            display.update()

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
