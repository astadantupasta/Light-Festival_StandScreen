from contextlib import redirect_stderr
import pygame, sys
from pygame.locals import *
import math
from IGame import IGame
from StepOn import StepOn
from Tile import Tile
from Matrix import Matrix
from Circle import Circle
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

length = 13

# Matrix for previous and current matrix state
previous_state = [[0 for x in range(length)] for y in range(length)]
current_state = [[0 for x in range(length)] for y in range(length)]

# Matrix initiation
matrix = Matrix()

# IGame initiation
game = Circle()
 
pygame.init()

# Set screen parameters
size = [660, 660]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Arial', 10)
grid_node_size = 50
rows_space = 5


def createSquare(x, y, tile):
    pygame.draw.rect(screen, tile.color, [x, y, grid_node_size, grid_node_size]) 
    screen.blit(font.render(str(tile.weight), True, GREY), (x+15, y+20))

    # Painting borders
    pygame.draw.rect(screen, WHITE, [x, y, grid_node_size, rows_space])
    pygame.draw.rect(screen, WHITE, [x, y, rows_space, grid_node_size])
    pygame.draw.rect(screen, WHITE, [x, grid_node_size, grid_node_size + rows_space, rows_space])
    pygame.draw.rect(screen, WHITE, [grid_node_size, y, rows_space, rows_space + grid_node_size])

def visualiseGrid():

    y1 = 0
    for x in range(length):
        x1 = 0
        for y in range(length):
            createSquare(x1, y1, matrix.get_tile(x, y))
            x1 += grid_node_size
        y1 += grid_node_size


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            y, x = pygame.mouse.get_pos()
            x  = math.trunc(x / 50)
            y  = math.trunc(y / 50)

            if(matrix.get_tile(x, y).weight > 500):
                matrix.get_tile(x, y).set_weight(0.0)
            else:
                matrix.get_tile(x, y).set_weight(1000.0)
    
    pygame.display.update()


def read_weights():
    """Reads the weights, reacts if someone steps on the tile.
    Return: (bool) True if at least one person stepped on the tile"""
    global previous_state, current_state
    stepped = False

    for x in range(length):

        for y in range(length):

            if matrix.get_tile(x, y).weight > 0: # CHECK CONDITION, IS IT ZERO?
                current_state[x][y] = 1
            if current_state[x][y] == 1 and previous_state[x][y] == 0:
                game.react_to_click(matrix, x, y)
                stepped = True
            else:
                 if current_state[x][y] == 0 and previous_state[x][y] == 1:
                    game.react_to_unclick(matrix, x, y)
    
    if type(game) is not StepOn:
        previous_state = current_state
    current_state = [[0 for x in range(length)] for y in range(length)]

    return stepped

screen.fill(WHITE)
pygame.display.set_caption("StandScreen")

# Game initiation
game = Circle()

# Variable for testing weather someone stepped on the tile
someone_did_step = False

# Saves times
current_time = pygame.time.get_ticks()
last_time_someone_stepped = pygame.time.get_ticks()
step_on_started = 0

# Booleans for types
step_on_is_on = False
circle_is_on = True

# Loop until the user clicks the close button.
done = False
while not done:
    visualiseGrid()
    current_time = pygame.time.get_ticks()
    someone_did_step = read_weights()

    if someone_did_step:
        last_time_someone_stepped = pygame.time.get_ticks()
    
    if (current_time - last_time_someone_stepped) > 10000:
        last_time_someone_stepped = pygame.time.get_ticks()
        step_on_started = pygame.time.get_ticks()
        game = StepOn()
        game.start_game(matrix)
        step_on_is_on = True

    if (step_on_is_on and (current_time - step_on_started) > 5000) or (step_on_is_on and someone_did_step):
        step_on_started = 0
        step_on_is_on = False
        game = Circle()
        game.start_game(matrix)

        if someone_did_step:
            someone_did_step = read_weights()

# Close everything down
pygame.quit()