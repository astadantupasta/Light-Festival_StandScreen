from abc import ABC, abstractmethod
import random
import colorsys
import pygame, sys

class IGame(ABC):
    @abstractmethod
    def start_game(self, matrix):
        pass

    @abstractmethod
    def end_game(self, matrix):
        pass

    @abstractmethod
    def react_to_click(self, x, y, matrix):
        pass

    @abstractmethod
    def react_to_unclick(self, x, y, matrix):
        pass

    def get_random_bright_color(self):
        """Gets a random birght color"""
        h, s, l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
        r, g, b = [int(256*i) for i in colorsys.hls_to_rgb(h, l, s)]
        color = (r, g, b)
        return color

    def wait(self, time):
        """Dealys code for a specified amount of seconds"""
        current_time = pygame.time.get_ticks()
        end_time = current_time + time * 1000

        while current_time < end_time:
            current_time = pygame.time.get_ticks()