import pygame
from pygame.sprite import Sprite

class Puzzle(Sprite):

    def __init__(self,image_path,answer,settings,screen):
        
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the puzzle image and get its rect attribute
        self.image = pygame.image.load(image_path)

        # return a width and height of an image
        self.size = self.image.get_size()
        # create a 2x bigger image than self.image
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

    """A class to represent a single raindrop."""
            
    def blitme(self):
        """Draw the raindrop at its current location."""
        # draw bigger image to screen at x=100 y=100 position
        #self.screen.blit(self.smaller_img, [100,100])
        self.screen.blit(self.image, self.rect)