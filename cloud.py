import pygame
import random as rand

class Cloud(pygame.sprite.Sprite):

    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = rand.randint(0, 400)

    def update(self, game_speed):

       # TODO start from here

