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

class Engine:

    def __init__(self, width: int = 1000, height: int = 800) -> None:
        '''
        Constructor

        Parameters: None

        Returns: None
        '''
        # initialize pygame assets
        pygame.init()

        # set window values
        self.w = width
        self.h = height
        self.window = display.set_mode((width, height))
        display.set_caption("Tetris Clone")

        # run game
        self.run_game()

    def run_game(self) -> None:
        '''
        Runs the main game loop.

        Parameters: None

        Returns: None
        '''
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit(0)

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."