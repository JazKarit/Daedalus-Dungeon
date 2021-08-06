import pygame
from pygame.sprite import Sprite
from perspective_transform import wall_transform
from answer_box import AnswerBox
import cv2
import numpy as np

class Door(Sprite):

    def __init__(self,door_image_path,puzzle_image_path,answer,settings,screen):
        
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image_path = puzzle_image_path[0:-4] + "_door.jpg"

        self.solved_image_path = door_image_path

        img = cv2.imread(door_image_path)
        puzzle_img = cv2.imread(puzzle_image_path)
        puzzle_img = cv2.resize(puzzle_img,(700,700))
        img[800:(800+puzzle_img.shape[0]), 550:(550+puzzle_img.shape[1])] = puzzle_img
        # img = img * np.array([0.6,0.6,1.2])
        cv2.imwrite(self.image_path,img)

        # Load the puzzle image and get its rect attribute
        self.image = pygame.image.load(self.image_path)
        self.orientation = 'center'

        # resize
        self.image = pygame.transform.scale(self.image, (500, 700))
        self.room_image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.room_rect = self.room_image.get_rect()


        # Start each new puzzle near the top left of the screen.
        self.rect.x = 430
        self.rect.y = 100
        self.room_rect.x = 200
        self.room_rect.y = 200
        self.answer = answer

        self.answer_box = AnswerBox(answer,765,600,30,30,settings,screen)
        self.is_solved = False

    def try_to_answer(self,trial_answer):

        if self.answer == trial_answer:
            print("Answer Correct!")

        else:
            print("Sorry wrong answer, try again")

    def save_perspective_image(self,orientation):
        if self.is_solved:
            cv2.imwrite(self.solved_image_path[0:-4] + '_' + orientation + '.jpg', wall_transform(self.solved_image_path,orientation))
        else: 
            cv2.imwrite(self.image_path[0:-4] + '_' + orientation + '.jpg', wall_transform(self.image_path,orientation)) 

    def set_orientation(self,orientation):

        self.orientation = orientation

        if orientation == 'back':
            self.room_rect.x = self.settings.screen_width
            self.room_rect.y = self.settings.screen_height
            return

        if self.is_solved:
            try:
                self.room_image = pygame.image.load(self.solved_image_path[0:-4] + '_' + orientation + '.jpg') 

            except:
                self.save_perspective_image(orientation)
                self.room_image = pygame.image.load(self.solved_image_path[0:-4] + '_' + orientation + '.jpg')
        else:
            try:
                self.room_image = pygame.image.load(self.image_path[0:-4] + '_' + orientation + '.jpg') 

            except:
                self.save_perspective_image(orientation)
                self.room_image = pygame.image.load(self.image_path[0:-4] + '_' + orientation + '.jpg')
        
        self.room_rect = self.room_image.get_rect()

        if orientation == 'left':
            self.room_rect.x = 100
            self.room_rect.y = 250
        elif orientation == 'center':
            self.room_rect.x = 650
            self.room_rect.y = 330
        elif orientation == 'right':
            self.room_rect.x = 1050
            self.room_rect.y = 250

    def set_as_solved(self):
        self.is_solved = True
        self.image = pygame.image.load(self.solved_image_path)

        # resize
        self.image = pygame.transform.scale(self.image, (500, 700))
        self.room_image = pygame.transform.scale(self.image, (300, 300))
        self.set_orientation(self.orientation)
        self.answer_box.is_invisible = True
    
    def blit_puzzle(self):
        self.screen.blit(self.image, self.rect)
        
    def blit_to_room(self):
        self.screen.blit(self.room_image, self.room_rect)