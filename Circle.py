
from IGame import IGame
from Tile import Tile
from Matrix import Matrix
import random
import colorsys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)


class Circle(IGame):
    """Colors the surrounding tiles of the one on which someone stepped
    in a random bright color"""
    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)

    def react_to_click(self, matrix, x, y):
       # matrix.get_tile(x, y).set_color(RED)

        color = self.get_random_bright_color()

        # Colors the XY-tile surrounding tiles in a random color
        for i in range(x-1, x+2):
            if i >= 0 and i < matrix.length:
                for j in range(y-1, y+2):
                    if j >= 0 and j < matrix.length:
                        matrix.get_tile(i, j).set_color(color)


    def react_to_unclick(self, matrix, x, y):
        # Turns off the light
        for i in range(x-1, x+2):
            if i >= 0 and i < matrix.length:
                for j in range(y-1, y+2):
                    if j >= 0 and j < matrix.length:
                        matrix.get_tile(i, j).set_color(BLACK)

    

