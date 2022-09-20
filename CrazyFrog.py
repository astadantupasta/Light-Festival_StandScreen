
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


class CrazyFrog(IGame):
    """Game: one needs to step on green tiles, and avoid the red ones"""

    def __init__(self):
        a3 = pygame.mixer.Sound("static\\piano\\a3.wav")
        a4 = pygame.mixer.Sound("static\\piano\\a4.wav")
        aa4 = pygame.mixer.Sound("static\\piano\\a-4.wav") # #A4
        b4 = pygame.mixer.Sound("static\\piano\\b4.wav")
        c4 = pygame.mixer.Sound("static\\piano\\c4.wav")
        d4 = pygame.mixer.Sound("static\\piano\\d4.wav")
        e4 = pygame.mixer.Sound("static\\piano\\e4.wav")
        f4 = pygame.mixer.Sound("static\\piano\\f4.wav")
        g4 = pygame.mixer.Sound("static\\piano\\g4.wav")
        d5 = pygame.mixer.Sound("static\\piano\\d5.wav")
        self.error = pygame.mixer.Sound("static\\music\\Mistake.wav")

        self.note_num = 0
        self.notes_sequnce = [d4, f4, d4, d4, g4, d4, c4, a4, d4, d4, #1
                            aa4, a4, f4, d4, a4, d5, d4, c4, c4, a3, e4, d4, #2
                            d4, f4, d4, d4, g4, d4, #3
                            c4, d4, a4, d4, d4, aa4, a4, f4, d4, a4, d5, d4, c4, #4
                            c4, a3, e4, d4, d4, #5
                            f4, d4, d4, g4, d4, c4, d4, a4, d4, d4, aa4, #6
                            a4, f4, d4, a4, d5, d4, c4, c4, a3, e4, d4, #7
                            d4, f4, d4, d4, g4, d4, c4, #8
                            d4, a4, d4, d4, aa4, a4, f4, d4, a4, d5, d4, c4, c4, #9
                            a3, e4, d4, #10
                            d4, f4, d4, d4, g4, d4, #11
                            c4, d4, a4, d4, d4, aa4, a4, f4, d4, a4, d5, d4, c4, #12
                            c4, a3, e4, d4, d4, #13
                            f4, d4, d4, g4, d4, c4, d4, a4, d4, d4, aa4, #14
                            a4, f4, d4, a4, d5, d4, c4, c4, a3, e4, d4] #15

    def get_music(self):
        pass

    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)
        self.color_tiles_in_red_and_green(matrix)

    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
        if matrix.get_tile(x, y).color == GREEN:
            pygame.mixer.Sound.play(self.notes_sequnce[self.note_num])
            print(self.notes_sequnce[self.note_num])
            print(self.note_num)
            self.note_num += 1
            if self.note_num >= len(self.notes_sequnce):
                self.note_num = 0

        else:
            if matrix.get_tile(x, y).color == RED:
                pygame.mixer.Sound.play(self.error)
        

    def react_to_standing(self, matrix, x, y):
        """Fade out the color"""
        r,g,b = matrix.get_tile(x, y).color
        if r == 0 and g == 0 and b == 0:
            return

        r -= 5
        g -= 5
        b -= 5

        if r < 0:
            r = 0

        if g < 0:
            g = 0

        if b < 0:
            b = 0
        
        matrix.get_tile(x, y).set_color((r,g,b))

    def color_tiles_in_red_and_green(self, matrix):
        """Randomly colors 80 tiles in RED and 20 tiles in GREEN.
        Tile is not being colored if someone is standing on it."""
        matrix.color_all(BLACK)

        for i in range(70):
            rand_x = random.randint(0, 12)
            rand_y = random.randint(0, 12)
            if matrix.get_tile(rand_x, rand_y).weight < 500: # cheeeeeeeeeeeech this condition
                matrix.get_tile(rand_x, rand_y).set_color(RED)
            
        for i in range(40):
            rand_x = random.randint(0, 12)
            rand_y = random.randint(0, 12)
            if matrix.get_tile(rand_x, rand_y).weight < 500:
                matrix.get_tile(rand_x, rand_y).set_color(GREEN)     


    def react_to_unclick(self, matrix, x, y):
        pass


    

