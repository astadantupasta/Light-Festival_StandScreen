
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

h,s,v = 0,1,1

class ChangingColors(IGame):
    """All the colors change gradually"""

    def get_music(self):
        return 'static\\music\\ChangingColors.wav'

    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)
        pygame.mixer.music.load(self.get_music())
        pygame.mixer.music.play(-1)

        for x in range(matrix.length):
            for y in range(matrix.length):
                global h,s,v
                h = ( h + 0.001 ) % 1
                color = list(colorsys.hsv_to_rgb(h,s,v))
                for c in range(len(color)):
                    color[c] = int(color[c]*255)
                matrix.get_tile(x, y).set_color(color)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
        global h,s,v
        h = h - 0.168

        for i in range(matrix.length):
            for j in range(matrix.length):
                h = ( h + 0.001 ) % 1
                color = list(colorsys.hsv_to_rgb(h,s,v))
                for c in range(len(color)):
                    color[c] = int(color[c]*255)
                matrix.get_tile(i, j).set_color(color)


    def react_to_unclick(self, matrix, x, y):
        matrix.disable_all_tiles(BLACK)
    

