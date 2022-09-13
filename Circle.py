
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


class Circle(IGame):
    """Colors the surrounding tiles of the one on which someone stepped
    in a random bright color"""
    def get_music(self):
        return 'static\\music\\NewGameStarted.wav'

    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)
        pygame.mixer.music.load(self.get_music())
        pygame.mixer.music.play(1)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
        pygame.mixer.Sound.play(matrix.get_tile(x, y).sound)

        color = self.get_random_bright_color()

        # Colors the XY-tile surrounding tiles in a random color
        for i in range(x-1, x+2):
            if i >= 0 and i < matrix.length:
                for j in range(y-1, y+2):
                    if j >= 0 and j < matrix.length:
                        if matrix.get_tile(i, j).weight < 500 or (x == i and y ==j):
                            matrix.get_tile(i, j).set_color(color)

    def react_to_standing(self, matrix, x, y):
        r,g,b = matrix.get_tile(x, y).color

        r -= 5
        g -= 5
        b -= 5

        if r < 0:
            r = 0

        if g < 0:
            g = 0

        if b < 0:
            b = 0
        
        color2 = (r, g, b)

        for i in range(x-1, x+2):
            if i >= 0 and i < matrix.length:
                for j in range(y-1, y+2):
                    if j >= 0 and j < matrix.length:
                        if (matrix.get_tile(i, j).weight < 500) or (x == i and y == j):
                            matrix.get_tile(i, j).set_color(color2)

    def react_to_unclick(self, matrix, x, y):
        # Turns off the light
        for i in range(x-1, x+2):
            if i >= 0 and i < matrix.length:
                for j in range(y-1, y+2):
                    if j >= 0 and j < matrix.length:
                        matrix.get_tile(i, j).set_color(BLACK)


    

