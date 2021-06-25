import pygame
from pygame.sprite import Group
import sys

from settings import Settings
from puzzle import Puzzle
from room import Room

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


    puzzles = [Puzzle('puzzle_door.jpg',4.8,settings,screen),Puzzle('puzzle_2.jpg',10.8,settings,screen),Puzzle('puzzle_3.jpg',66,settings,screen)]
    puzzles[0].set_orientation('center')
    puzzles[1].set_orientation('left')
    puzzles[2].set_orientation('right')

    my_room = Room(puzzles)
    
    dots = []
    drawing = False
    settings.current_room = my_room
    mouse_x,mouse_y = 0,0
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and settings.view == 'puzzle_view':  
                drawing = True
                dots.append([])
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
                if settings.view == 'room_view': 
                    mouse_x, mouse_y = event.pos
                    puzzle_clicked = settings.current_room.get_puzzle_clicked(mouse_x,mouse_y)
                    if puzzle_clicked:
                        settings.view = 'puzzle_view'
                        settings.current_puzzle = puzzle_clicked
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and settings.view == 'puzzle_view':
                    drawing = False
                    if dots: 
                        dots.pop()
                elif event.key == pygame.K_ESCAPE:
                    settings.view = 'room_view'
                    settings.current_puzzle = None
                    dots = []
            elif event.type == pygame.MOUSEBUTTONUP and settings.view == 'room_view': 
                mouse_x,mouse_y = event.pos
                puzzle_clicked = settings.current_room.get_puzzle_clicked(mouse_x,mouse_y)
                if puzzle_clicked:
                    settings.view = 'puzzle_view'
                    settings.current_puzzle = puzzle_clicked
                
        
        if settings.view == 'room_view':
            settings.current_room.draw()
        elif settings.view == 'puzzle_view':
            settings.current_puzzle.blit_puzzle()
        mouse_pos = pygame.mouse.get_pos()        
        if drawing:
            dots[-1].append(mouse_pos)
        for dot_array in dots:
            if(len(dot_array) > 4):
                pygame.draw.lines(screen, (0, 0, 0), False, dot_array) 

        pygame.display.flip()
        

run_game()

# my_list = ['red','blue','green']
# list2 = my_list.copy()
# list2.append('yellow')
# print('my_list: ' + str(my_list))
# print('List2: ' + str(list2))