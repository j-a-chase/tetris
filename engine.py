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
from lib import get_shapes_arr, update_board, clear_completed_rows, check_collision, check_rotation, game_over
from copy import copy

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
        self.score = 0
        self.bonus_threshold = 3000

        self.shapes_arr = get_shapes_arr()
        
        # render fonts
        self.score_font = pygame.font.SysFont("impact", 50)
        self.description_font = pygame.font.SysFont('timesnewroman', 20)

        # prerender score text
        self.score_text = self.score_font.render(f'{self.score}', 1, self.LINE_COLOR)

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
    
    def update_score(self, add: int) -> None:
        '''
        Updates the score rendering.

        Parameters:
            - add: an integer indicating how much to increment the score by.

        Returns: None
        '''
        self.score += add
        self.score_text = self.score_font.render(f'{self.score}', 1, self.LINE_COLOR)

    def run_game(self) -> None:
        '''
        Runs the main game loop.

        Parameters: None

        Returns: None
        '''
        self.window.fill(self.BG_COLOR)
        self.draw_grid()
        self.window.blit(self.score_text, 
                         (self.GRID_OFFSET_X + (self.GRID_SIZE * self.COLUMNS) + 300,
                          self.GRID_OFFSET_Y + (self.GRID_SIZE * self.ROWS // 2)))
        display.update()

        tetrimino = Figure('I', self.TEST_SHAPE_COLOR)
        move_timer = 0
        bonus_timer = 0
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
                        while not check_collision(self.board, tetrimino, self.ROWS): tetrimino.move(0, 1)

                    if event.key == pygame.K_UP:
                        rotated = copy(tetrimino)
                        rotated.rotate()
                        if check_rotation(self.board, rotated, self.COLUMNS, self.ROWS): tetrimino.rotate()

            move_timer += 1
            bonus_timer += 1
            if move_timer >= self.move_delay:
                tetrimino.move(0, 1)
                move_timer = 0

            if check_collision(self.board, tetrimino, self.ROWS):
                update_board(self.board, tetrimino)
                tetrimino = Figure(choice(self.shapes_arr), self.TEST_SHAPE_COLOR)

                clear_count = clear_completed_rows(self.board, self.COLUMNS)
                time_multiplier = 1.5 if bonus_timer < self.bonus_threshold else 1
                if clear_count > 0:
                    print(f'{clear_count} rows cleared.')
                    if clear_count == 1:
                        self.update_score(int(100 * time_multiplier))
                    elif clear_count == 2:
                        self.update_score(int(300 * time_multiplier))
                    elif clear_count == 3:
                        self.update_score(int(500 * time_multiplier))
                    else:
                        self.update_score(int(800 * time_multiplier))
                    bonus_timer = 0

                if game_over(self.board, tetrimino):
                    print('GAME OVER')
                    gameover_text = self.score_font.render("GAME OVER!", 1, self.LINE_COLOR)
                    self.window.blit(gameover_text,
                                     (self.GRID_OFFSET_X + (self.GRID_SIZE * self.COLUMNS) // 8,
                                      self.GRID_OFFSET_Y + (self.GRID_SIZE * self.ROWS)))
                    help_text = self.description_font.render('Press Q to quit - Press Enter to Play Again', 1, self.LINE_COLOR)
                    self.window.blit(help_text,
                                     (self.GRID_OFFSET_X * .9,
                                      (self.GRID_OFFSET_Y * 2) + (self.GRID_SIZE * self.ROWS)))
                    display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit(0)

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    self.update_score(-self.score)
                                    self.board = [[0] * self.COLUMNS for _ in range(self.ROWS)]
                                    self.run_game()

                                if event.key == pygame.K_q:
                                    pygame.quit()
                                    exit(0)
                                

            self.window.fill(self.BG_COLOR)
            self.draw_figure(tetrimino)
            self.draw_grid()
            self.window.blit(self.score_text, 
                            (self.GRID_OFFSET_X + (self.GRID_SIZE * self.COLUMNS) + 300,
                            self.GRID_OFFSET_Y + (self.GRID_SIZE * self.ROWS // 2)))
            display.update()

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
