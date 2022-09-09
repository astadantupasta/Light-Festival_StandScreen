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
    port_index: (float) led strip port's index
    enabled: (bool) is player allowed to step on the tile. If the tile is disabled,
                nothing happens when one steps on it
    weight: (float)
    """

    def __init__(self, controller_address, port_index):
        self.controller_address = controller_address
        self.color = BLACK
        self.port_index = port_index
        self.enabled = False
        self.weight = 0.0
    

    
    def is_pressed(self):
        return self.weight > 0

    def set_controller_address(self, address):
        self.controller_address = address

    def set_port_index(self, index):
        self.port_index = index
    
    def set_color(self, color):
        self.color = color
    
    def set_weight(self, weight):
        self.weight = weight

    def enable(self, color):
        self.enabled = True
        self.color = color

    def disable(self, color):
        self.enabled = False
        self.color = color