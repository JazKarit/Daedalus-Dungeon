import pygame
from pygame.sprite import Sprite
from perspective_transform import wall_transform
import cv2

class Room():

    def __init__(self,puzzles):
        self.puzzles = puzzles

    def draw(self):
        for puzzle in self.puzzles:
            puzzle.blitme()