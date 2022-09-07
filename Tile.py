import pygame
from pygame import Rect

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (30, 144, 255)
GREEN = (0, 255, 0)

class Tile:

    """
    A class used to gather data of a tile
    controller_address: (int)
    color: (color) color of the tile
    port_index: (float) sensor and led strip port's index
    x: (int) x coordinate
    y: (int) y coordinate
    enabled: (bool) is player allowed to step on the tile. If the tile is disabled,
                nothing happens when one steps on it
    """

    def __init__(self, controller_address, color, port_index, x, y, enabled):
        self.controller_address = controller_address
        self.color = color
        self.port_index = port_index
        self.x = x
        self.y = y
        self.enabled = True
    
    def __init__(self, x, y):
        self.controller_address = 0
        self.color = BLACK
        self.port_index = 0.0
        self.x = x
        self.y = y
        self.enabled = False
    
    def is_pressed(self):
        return self.port_index > 0

    def set_controller_address(self, address):
        self.controller_address = address

    def set_port_index(self, index):
        self.port_index = index
    
    def set_color(self, color):
        self.color = color

    def enable(self, color):
        self.enabled = True
        self.color = color

    def disable(self, color):
        self.enabled = False
        self.color = color