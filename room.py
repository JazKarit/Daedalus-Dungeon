import pygame
from pygame.sprite import Sprite
from perspective_transform import wall_transform
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