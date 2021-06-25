import pygame
from pygame.sprite import Sprite
from perspective_transform import wall_transform
import cv2

class Puzzle(Sprite):

    def __init__(self,image_path,answer,settings,screen):
        
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the puzzle image and get its rect attribute
        self.image = pygame.image.load(image_path)
        self.orientation = 'center'

        # return a width and height of an image
        self.size = self.image.get_size()
        # resize
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()

        # Start each new puzzle near the top left of the screen.
        self.rect.x = 200
        self.rect.y = 200
        self.image_path  = image_path
        self.answer = answer

    def try_to_answer(self,trial_answer):

        if self.answer == trial_answer:
            print("Answer Correct!")

        else:
            print("Sorry wrong answer, try again")

    def save_perspective_image(self,orientation):
        cv2.imwrite(self.image_path+"_"+orientation,wall_transform(self.image_path,orientation))

    def set_orientation(self,orientation):

        try:
            self.image = pygame.image.load(self.image_path + '_' + orientation)

        except:
            self.save_perspective_image(orientation)
            self.image = pygame.image.load(self.image_path + '_' + orientation)
        
        if orientation == 'left':
            self.rect.x = 100
            self.rect.y = 250
        elif orientation == 'center':
            self.rect.x = 670
            self.rect.y = 350
        elif orientation == 'right':
            self.rect.x = 1050
            self.rect.y = 250
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)