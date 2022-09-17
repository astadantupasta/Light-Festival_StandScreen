from contextlib import redirect_stderr
import pygame, sys
from pygame.locals import *
import math
from ChangingColors import ChangingColors
from IGame import IGame
from PrintText import PrintText
from Tile import Tile
from Matrix import Matrix
from Circle import Circle
from Intro_ShowYourStripes import Intro
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

length = 13

# Matrix for previous and current matrix state
previous_matrix_state = [[0 for x in range(length)] for y in range(length)]
current_matrix_state = [[0 for x in range(length)] for y in range(length)]
 
pygame.init()

# Matrix initiation
matrix = Matrix()

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

        # When someone clicked the mouse button    
        if event.type == MOUSEBUTTONUP:
            # Get mouse possition and calculate x and y coordinates of the matrix
            y, x = pygame.mouse.get_pos()
            x  = math.trunc(x / 50)
            y  = math.trunc(y / 50)

            # If the tile already has weight, then the click 
            # means that someone stood out of the tile
            if(matrix.get_tile(x, y).weight > 500):
                matrix.get_tile(x, y).set_weight(0.0)
            else:
                matrix.get_tile(x, y).set_weight(1000.0)
    
    pygame.display.update()


def read_weights():
    """Reads the weights, reacts if someone steps on the tile.
    Return: (bool) True if at least one person stepped on the tile"""
    global previous_matrix_state, current_matrix_state
    stepped = False

    for x in range(length):

        for y in range(length):

            if matrix.get_tile(x, y).weight > 500: # CHECK CONDITION, IS IT 500?
                current_matrix_state[x][y] = 1
            if current_matrix_state[x][y] == 1 and previous_matrix_state[x][y] == 0:
                game.react_to_click(matrix, x, y)
                stepped = True
            else:
                if current_matrix_state[x][y] == 0 and previous_matrix_state[x][y] == 1:
                    game.react_to_unclick(matrix, x, y)
                else:
                    if current_matrix_state[x][y] == 1 and previous_matrix_state[x][y] == 1 and (type(game) is Circle):
                        if matrix.get_tile(x,y).color != (0,0,0):
                            game.react_to_standing(matrix, x, y)
                            clock.tick(200)
    
    # If the game is not the one, which turns on only when installation's participants are absent
    if (type(game) is not PrintText) and (type(game) is not ChangingColors) :
        previous_matrix_state = current_matrix_state
    current_matrix_state = [[0 for x in range(length)] for y in range(length)]

    return stepped

def randomly_generate_weights():
    """Method for testing the code"""
    for x in range(matrix.length):
        for y in range(matrix.length):
            matrix.get_tile(x,y).set_weight(random.randint(0,501))

def get_real_weights():
    """Method for getting the real weights"""
    for x in range(matrix.length):
        for y in range(matrix.length):
            matrix.get_tile(x,y).get_weight()


screen.fill(WHITE)
pygame.display.set_caption("StandScreen")

# Game initiation
game = Intro()

# Variable for testing weather someone stepped on the tile
someone_did_step = False

# Save timestamps
current_time = pygame.time.get_ticks()
last_tile_trigger_timestamp = pygame.time.get_ticks()
beginning_timestamp = pygame.time.get_ticks()
intro_started_timestamp = 0
print_text_started_timestamp = 0

# Variables for ChangingColors
last_rand_tile_color_in_red_timestamp = pygame.time.get_ticks()
rand_x = random.randint(0,12)
rand_y = random.randint(0,12)

# Booleans for different games/animations
print_text_is_on = False
circle_is_on = False
changing_colors_is_on = False
intro_is_on = False

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
while not done:
    visualiseGrid()
    # UNCOMMENT WHEN TESTING WITH RANDOM VALUES
    # randomly_generate_weights()

    # UNCOMMENT WHEN READING THE REEEEEEEEEEEAL WEIGHTS
    # get_real_weights()

    current_time = pygame.time.get_ticks()
    someone_did_step = read_weights()

    # First 50 sek. Or games going for 10 mins? Start Intro animation
    if ((current_time - beginning_timestamp) < 58000 or (current_time - intro_started_timestamp) > 658000) and not intro_is_on:
        # Print numbers 3 to 1
        game = PrintText()
        game.start_game(matrix)

        game.paint_letters(matrix, 2)
        visualiseGrid()
        pygame.time.delay(5000)

        game.paint_letters(matrix, 6)
        visualiseGrid()
        pygame.time.delay(1000)

        game.paint_letters(matrix, 5)
        visualiseGrid()
        pygame.time.delay(1000)

        game.paint_letters(matrix, 4)
        visualiseGrid()
        pygame.time.delay(1000)

        # Start animation
        game.end_game(matrix)
        game = Intro()
        game.start_game(matrix)
        intro_started_timestamp = pygame.time.get_ticks()
        intro_is_on = True

    # Is Intro animation going?
    if intro_is_on:
        game.react_to_click(matrix, 0, 0)

        if (current_time - intro_started_timestamp) < 16000:
            clock.tick(2)
        else:
            if (current_time - intro_started_timestamp) < 25000:
                clock.tick(4)
            else:
                clock.tick(60)
        
        # Animation time elapsed? Print numbers from 3 to 1
        if (current_time - intro_started_timestamp) > 50000:
            intro_is_on = False
            game.end_game(matrix)

            game = PrintText()
            game.start_game(matrix)

            game.paint_letters(matrix, 6)
            visualiseGrid()
            pygame.time.delay(1000)

            game.paint_letters(matrix, 5)
            visualiseGrid()
            pygame.time.delay(1000)

            game.paint_letters(matrix, 4)
            visualiseGrid()
            pygame.time.delay(1000)

            game.paint_letters(matrix, 1)

            last_tile_trigger_timestamp = pygame.time.get_ticks()
            print_text_started_timestamp = pygame.time.get_ticks()
            print_text_is_on = True
        continue
 

    if someone_did_step:
        last_tile_trigger_timestamp = pygame.time.get_ticks()

        # Animation in on? Start the game
        if (print_text_is_on or changing_colors_is_on):
            print_text_started_timestamp = 0
            print_text_is_on = False
            changing_colors_is_on = False

            game = Circle()
            game.start_game(matrix)

            someone_did_step = read_weights()
        continue
            
    # No interaction with the installation for 10 seconds? Turn on PrintText: STEP ON
    if (current_time - last_tile_trigger_timestamp) > 30000:
        game.end_game(matrix)
        changing_colors_is_on = False
        last_tile_trigger_timestamp = pygame.time.get_ticks()
        print_text_started_timestamp = pygame.time.get_ticks()
        game = PrintText()
        game.start_game(matrix)
        game.paint_letters(matrix, 1)
        print_text_is_on = True

        continue

    # PrintText taking longer than 5 sec? Start the ChangingColors
    if (print_text_is_on and (current_time - print_text_started_timestamp) > 5000):
        game.end_game(matrix)
        print_text_started = 0
        print_text_is_on = False
        changing_colors_is_on = True
        game = ChangingColors()
        game.start_game(matrix)

    # Changing colors is on?
    if changing_colors_is_on:
        clock.tick(60)
        game.react_to_click(matrix,0,0)
        matrix.get_tile(rand_x, rand_y).set_color(RED)
        if (current_time - last_rand_tile_color_in_red_timestamp) > 460:
            rand_x = random.randint(0,12)
            rand_y = random.randint(0,12)
            last_rand_tile_color_in_red_timestamp = pygame.time.get_ticks()
        
        continue



# Close everything down
pygame.quit()