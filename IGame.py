from abc import ABC, abstractmethod
import random
import colorsys
import pygame, sys

class IGame(ABC):
    @abstractmethod
    def get_music(self):
        pass

    @abstractmethod
    def start_game(self, matrix):
        pass

    @abstractmethod
    def end_game(self, matrix):
        pass

    @abstractmethod
    def react_to_click(self, matrix, x, y):
        pass

    @abstractmethod
    def react_to_standing(self, matrix, x, y):
        pass

    @abstractmethod
    def react_to_unclick(self, matrix, x, y):
        pass

    def get_random_bright_color(self):
        """Gets a random birght color"""
        h, s, l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
        r, g, b = [int(256*i) for i in colorsys.hls_to_rgb(h, l, s)]
        color = (r, g, b)
        return color