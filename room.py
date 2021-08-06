import pygame
from pygame.sprite import Sprite
import cv2

class Room():

    def __init__(self,puzzles):
        self.puzzles = puzzles

    def draw(self):
        for puzzle in self.puzzles:
            puzzle.blit_to_room()

    def get_puzzle_clicked(self,mouse_x,mouse_y):
        for puzzle in self.puzzles:
            if puzzle.room_rect.collidepoint(mouse_x,mouse_y):
                return puzzle
        return None

    def turn_left(self):
        for puzzle in self.puzzles:
            if puzzle.orientation == 'left':
                puzzle.set_orientation('center')
            elif puzzle.orientation == 'center':
                puzzle.set_orientation('right')
            elif puzzle.orientation == 'right':
                puzzle.set_orientation('back')
            elif puzzle.orientation == 'back':
                puzzle.set_orientation('left')

    def turn_right(self):
        for puzzle in self.puzzles:
            if puzzle.orientation == 'left':
                puzzle.set_orientation('back')
            elif puzzle.orientation == 'center':
                puzzle.set_orientation('left')
            elif puzzle.orientation == 'right':
                puzzle.set_orientation('center')
            elif puzzle.orientation == 'back':
                puzzle.set_orientation('right')

    def get_room_in_orientation(self, orientation):
        for puzzle in self.puzzles:
            if puzzle.orientation == orientation:
                return puzzle