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
        color = figure.color
        shape = figure.shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell: pygame.draw.rect(self.window, color, (self.GRID_OFFSET_X + figure.x * self.GRID_SIZE + x * self.GRID_SIZE, self.GRID_OFFSET_Y + figure.y * self.GRID_SIZE + y * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

    def run_game(self) -> None:
        '''
        Runs the main game loop.

        Parameters: None

        Returns: None
        '''
        self.window.fill(self.BG_COLOR)
        self.draw_grid()
        display.update()
        test = Figure('I', self.TEST_SHAPE_COLOR)
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
                        if test.x == 10 - len(test.shape[0]): continue
                        test.move(1,0)

                    if event.key == pygame.K_LEFT:
                        if test.x == 0: continue
                        test.move(-1, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            test.move(0, 1)

            self.window.fill(self.BG_COLOR)
            self.draw_grid()
            self.draw_figure(test)
            print(test.x, test.y)
            display.update()
            pygame.time.delay(500)

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."