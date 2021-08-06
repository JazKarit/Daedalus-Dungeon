import pygame
from pygame.sprite import Group
import sys
import time

from settings import Settings
from door import Door
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


    # puzzles = [Puzzle('puzzles/graph_walk_puzzle.jpg',4.8,settings,screen),Puzzle('puzzles/hex_puzzle.jpg',10.8,settings,screen),Puzzle('puzzles/puzzle_door.jpg',66,settings,screen)]
    puzzles = [Door('art/locked_door.bmp','puzzles/graph_walk_puzzle.jpg',4.8,settings,screen),
               Door('art/locked_door.bmp','puzzles/hex_puzzle.jpg',10.8,settings,screen),
               Door('art/locked_door.bmp','puzzles/puzzle_door.jpg',66,settings,screen)]
    puzzles[0].set_orientation('center')
    puzzles[1].set_orientation('left')
    puzzles[2].set_orientation('right')

    my_room = Room(puzzles)
    
    strokes = []
    drawing = False
    settings.current_room = my_room
    mouse_x,mouse_y = 0,0
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_color)
        
        for event in pygame.event.get():
            if settings.view == 'puzzle_view':
                result = settings.current_puzzle.answer_box.handle_event(event)
                if result == 'correct':
                    print("That's correct!")
                elif result == 'wrong':
                    print("Sorry, incorrect")
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and settings.view == 'puzzle_view':  
                drawing = True
                strokes.append([])
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
                    if strokes: 
                        strokes.pop()
                elif event.key == pygame.K_ESCAPE:
                    settings.view = 'room_view'
                    settings.current_puzzle = None
                    strokes = []
                
        
        if settings.view == 'room_view':
            settings.current_room.draw()
        elif settings.view == 'puzzle_view':
            settings.current_puzzle.blit_puzzle()
            settings.current_puzzle.answer_box.update()
            settings.current_puzzle.answer_box.draw(screen)

        mouse_pos = pygame.mouse.get_pos()        
        if drawing:
            strokes[-1].append(mouse_pos)
        for dot_list in strokes:
            if(len(dot_list) > 4):
                pygame.draw.lines(screen, (0, 0, 0), False, dot_list) 

        

        pygame.display.flip()
        
        

run_game()