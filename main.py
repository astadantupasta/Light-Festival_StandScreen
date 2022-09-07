from contextlib import redirect_stderr
import pygame, sys
from pygame.locals import *
import math
from Tile import Tile
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

size = 13

# Matrix initiation
matrix = [[0 for x in range(size)] for y in range(size)]
for x in range(size):
    for y in range(size):
        matrix[x][y] = Tile(x, y)
 
pygame.init()

# Set the height and width of the screen
size = [660, 660]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Arial', 10)
grid_node_size = 50
rows_space = 5


def createSquare(x, y, tile):
    pygame.draw.rect(screen, tile.color, [x, y, grid_node_size, grid_node_size]) 
    screen.blit(font.render(str(tile.port_index), True, GREY), (x+15, y+20))

    # Painting borders
    pygame.draw.rect(screen, WHITE, [x, y, grid_node_size, rows_space])
    pygame.draw.rect(screen, WHITE, [x, y, rows_space, grid_node_size])
    pygame.draw.rect(screen, WHITE, [x, grid_node_size, grid_node_size + rows_space, rows_space])
    pygame.draw.rect(screen, WHITE, [grid_node_size, y, rows_space, rows_space + grid_node_size])

def visualiseGrid():
    y = 0
    for row in matrix:
        x = 0
        for tile in row:
            createSquare(x, y, tile)
            x += grid_node_size
        y += grid_node_size

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            y, x = pygame.mouse.get_pos()
            x  = math.trunc(x / 50)
            y  = math.trunc(y / 50)

            matrix[x][y].set_color(RED)
    
    pygame.display.update()


screen.fill(WHITE)
pygame.display.set_caption("StandScreen")

# Loop until the user clicks the close button.
done = False
while not done:
    visualiseGrid()

# Close everything down
pygame.quit()