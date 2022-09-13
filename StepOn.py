
from IGame import IGame
from Tile import Tile
from Matrix import Matrix
import random
import colorsys
import time
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
FIRST = (0, 0, 255)
SECOND = (204, 0, 204)


class StepOn(IGame):
    """Writes on the matrix STEP ON"""

    def get_music(self):
        return 'static\\music\\StepOn.wav'

    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)
        pygame.mixer.music.load(self.get_music())
        pygame.mixer.music.play(-1)

        # Writing STEP ON

        # S
        matrix.get_tile(1, 0).set_color(FIRST)
        matrix.get_tile(1, 1).set_color(FIRST)
        matrix.get_tile(1, 2).set_color(FIRST)
        matrix.get_tile(2, 0).set_color(FIRST)
        matrix.get_tile(3, 0).set_color(FIRST)
        matrix.get_tile(3, 1).set_color(FIRST)
        matrix.get_tile(3, 2).set_color(FIRST)
        matrix.get_tile(4, 2).set_color(FIRST)
        matrix.get_tile(5, 0).set_color(FIRST)
        matrix.get_tile(5, 1).set_color(FIRST)
        matrix.get_tile(5, 2).set_color(FIRST)
        
        # T
        matrix.get_tile(1, 3).set_color(SECOND)
        matrix.get_tile(1, 4).set_color(SECOND)
        matrix.get_tile(1, 5).set_color(SECOND)
        matrix.get_tile(2, 4).set_color(SECOND)
        matrix.get_tile(3, 4).set_color(SECOND)
        matrix.get_tile(4, 4).set_color(SECOND)
        matrix.get_tile(5, 4).set_color(SECOND)

        # E
        matrix.get_tile(1, 6).set_color(FIRST)
        matrix.get_tile(1, 7).set_color(FIRST)
        matrix.get_tile(1, 8).set_color(FIRST)
        matrix.get_tile(2, 6).set_color(FIRST)
        matrix.get_tile(3, 6).set_color(FIRST)
        matrix.get_tile(3, 7).set_color(FIRST)
        matrix.get_tile(3, 8).set_color(FIRST)
        matrix.get_tile(4, 6).set_color(FIRST)
        matrix.get_tile(5, 6).set_color(FIRST)
        matrix.get_tile(5, 7).set_color(FIRST)
        matrix.get_tile(5, 8).set_color(FIRST)
    
        # P
        matrix.get_tile(1, 9).set_color(SECOND)
        matrix.get_tile(1, 10).set_color(SECOND)
        matrix.get_tile(1, 11).set_color(SECOND)
        matrix.get_tile(2, 9).set_color(SECOND)
        matrix.get_tile(2, 11).set_color(SECOND)
        matrix.get_tile(3, 9).set_color(SECOND)
        matrix.get_tile(3, 10).set_color(SECOND)
        matrix.get_tile(3, 11).set_color(SECOND)
        matrix.get_tile(4, 9).set_color(SECOND)
        matrix.get_tile(5, 9).set_color(SECOND)

        # o
        matrix.get_tile(7, 2).set_color(FIRST)
        matrix.get_tile(7, 3).set_color(FIRST)
        matrix.get_tile(7, 4).set_color(FIRST)
        matrix.get_tile(8, 2).set_color(FIRST)
        matrix.get_tile(8, 4).set_color(FIRST)
        matrix.get_tile(9, 2).set_color(FIRST)
        matrix.get_tile(9, 4).set_color(FIRST)
        matrix.get_tile(10, 2).set_color(FIRST)
        matrix.get_tile(10, 4).set_color(FIRST)
        matrix.get_tile(11, 2).set_color(FIRST)
        matrix.get_tile(11, 3).set_color(FIRST)
        matrix.get_tile(11, 4).set_color(FIRST)

        # N
        matrix.get_tile(7, 6).set_color(SECOND)
        matrix.get_tile(8, 6).set_color(SECOND)
        matrix.get_tile(9, 6).set_color(SECOND)
        matrix.get_tile(10, 6).set_color(SECOND)
        matrix.get_tile(11, 6).set_color(SECOND)
        matrix.get_tile(7, 7).set_color(SECOND)
        matrix.get_tile(7, 8).set_color(SECOND)
        matrix.get_tile(8, 8).set_color(SECOND)
        matrix.get_tile(9, 8).set_color(SECOND)
        matrix.get_tile(10, 8).set_color(SECOND)
        matrix.get_tile(11, 8).set_color(SECOND)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
       matrix.disable_all_tiles(BLACK)

    def react_to_unclick(self, matrix, x, y):
        pass

    def react_to_standing(self, matrix, x, y):
        pass

    

