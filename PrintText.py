
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
C_50 = (51, 255, 255)
ONE_GREEN = (0, 255, 0)
TWO_PINK = (255, 0, 127)
THREE_BLUE = (0, 0, 225)
CYAN = (51, 255, 255)


class PrintText(IGame):
    """Writes on the matrix STEP ON"""

    def __init__(self):
        # S E O letters for STEOP ON
        self.s_e_o_ = [[1, 0], [1, 1], [1, 2], [2, 0], [3, 0], [3, 1], [3, 2], [4, 2], [5, 0], [5, 1], [5, 2],
                        [1, 6], [1, 7], [1, 8], [2, 6], [3, 6], [3, 7], [3, 8], [4, 6], [5, 6], [5, 7], [5, 8],
                        [7, 2], [7, 3], [7, 4], [8, 2], [8, 4], [9, 2], [9, 4], [10, 2], [10, 4], [11, 2], [11, 3], [11, 4]]

        # T P N letters for STEP ON
        self._t_p_n = [[1, 3], [1, 4], [1, 5], [2, 4], [3, 4], [4, 4], [5, 4], 
                        [1, 9], [1, 10], [1, 11], [2, 9], [2, 11], [3, 9], [3, 10], [3, 11], [4, 9], [5, 9],
                        [7, 6], [7, 7], [7, 8], [8, 6], [8, 8], [9, 6], [9, 8], [10, 6], [10, 8], [11, 6], [11, 8]]  

        # S E O F letters for STEP OFF
        self.s_e_o_f = [[1, 0], [1, 1], [1, 2], [2, 0], [3, 0], [3, 1], [3, 2], [4, 2], [5, 0], [5, 1], [5, 2],
                        [1, 6], [1, 7], [1, 8], [2, 6], [3, 6], [3, 7], [3, 8], [4, 6], [5, 6], [5, 7], [5, 8],
                        [7, 1], [7, 2], [7, 3], [8, 1], [8, 3], [9, 1], [9, 3], [10, 1], [10, 3], [11, 1], [11, 2], [11, 3],
                        [7, 7], [7, 8], [7, 9], [8, 7], [9, 7], [9, 8], [9, 9], [10, 7], [11, 7]]      

        # T P F letters for STEP OFF
        self._t_p_f_ = [[1, 3], [1, 4], [1, 5], [2, 4], [3, 4], [4, 4], [5, 4], 
                        [1, 9], [1, 10], [1, 11], [2, 9], [2, 11], [3, 9], [3, 10], [3, 11], [4, 9], [5, 9],
                        [7, 4], [7, 5], [7, 6], [8, 4], [9, 4], [9, 5], [9, 6], [10, 4], [11, 4]]
        
        # Number 50
        self.n_50 = [[3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [5, 2], [6, 2], [6, 3], [6, 4], [6, 5], [7, 5], [8, 5], [9, 2], [9, 3], [9, 4], [9, 5],
                    [3, 7], [3, 8], [3, 9], [3, 10], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [9, 8], [9, 9], [9, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10]]

        # Number 1
        self.n_1 = [[2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [3, 6], [3, 7],
                    [4, 6], [4, 7], [5, 6], [5, 7], [6, 6], [6, 7], [7, 6], [7, 7], 
                    [8, 6], [8, 7], [9, 6], [9, 7], [10, 6], [10, 7], [11, 6], [11, 7]]
        
        # Number 2
        self.n_2 = [[2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
                    [4, 8], [4, 9], [5, 8], [5, 9], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], 
                    [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 4], [8, 5], [9, 4], [9, 5],
                    [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9]]

        # Number 3
        self.n_3 = [[2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], 
                    [4, 8], [4, 9], [5, 8], [5, 9], [6, 4], [6, 5], [6, 6], [6, 7], [6, 9], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
                    [8, 8], [8, 9], [9, 8], [9, 9], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], 
                    [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [6, 8]]

    def get_music(self):
        return 'static\\music\\PrintText.wav'

    def start_game(self, matrix):
        matrix.enable_all_tiles(BLACK)
        pygame.mixer.music.load(self.get_music())
        pygame.mixer.music.play(-1)
        
    def paint_letters(self, matrix, text_to_print):
        """Paints the text chosen:
        text_to_print: (int)
        Meanings: 
        1 - print 'STEP ON'; 
        2 - print 'STEP OFF'; 
        3 - print '50';
        4 - print '1';
        5 - print '2';
        6 - print '3'"""
        matrix.color_all(BLACK)

        # STEP ON
        if text_to_print == 1:
            matrix.color_given_tiles(self.s_e_o_, FIRST)
            matrix.color_given_tiles(self._t_p_n, SECOND)
            return

        # STEP OFF
        if text_to_print == 2:
            matrix.color_given_tiles(self.s_e_o_f, FIRST)
            matrix.color_given_tiles(self._t_p_f_, SECOND)
            return

        # 50
        if text_to_print == 3:
            matrix.color_given_tiles(self.n_50, C_50)
            return
        
        # 1
        if text_to_print == 4:
            matrix.color_given_tiles(self.n_1, ONE_GREEN)
            matrix.color_row(0, CYAN)
            matrix.color_column(0, CYAN)
            return

        # 2
        if text_to_print == 5:
            matrix.color_given_tiles(self.n_2, TWO_PINK)
            matrix.color_row(0, CYAN)
            matrix.color_column(0, CYAN)
            return

        # 3
        if text_to_print == 6:
            matrix.color_given_tiles(self.n_3, THREE_BLUE)
            matrix.color_row(0, CYAN)
            matrix.color_column(0, CYAN)
            return


    def end_game(self, matrix):
        matrix.disable_all_tiles(BLACK)
        pygame.mixer.music.stop()

    def react_to_click(self, matrix, x, y):
       matrix.disable_all_tiles(BLACK)

    def react_to_unclick(self, matrix, x, y):
        pass

    def react_to_standing(self, matrix, x, y):
        pass

    

