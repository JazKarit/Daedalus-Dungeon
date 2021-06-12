import pygame
from pygame.sprite import Group
import sys

from settings import Settings
from puzzle import Puzzle

class Room:

    def __init__(self,puzzle_list):
        
        self.puzzle_list = puzzle_list
        

# my_puzzle = Puzzle('puzzle_door.jpg',42)

# my_puzzle.try_to_answer(42)


# my_puzzle_list = [my_puzzle]

# room = Room(my_puzzle_list)

def run_game():


    # Initialize game and create a screen object.
    pygame.init()
    
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Daedalus' Dungeon")


    my_puzzle = Puzzle('puzzle_door.bmp',42,settings,screen)
   
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sys.exit()

        # Make the most recently drawn screen visible.
        my_puzzle.blitme()
        pygame.display.flip()

run_game()

# my_list = ['red','blue','green']
# list2 = my_list.copy()
# list2.append('yellow')
# print('my_list: ' + str(my_list))
# print('List2: ' + str(list2))