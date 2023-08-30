import pygame

class Bird:

    def __init__(self):
        self.x = 400
        self.y = 260
        self.FLYING = [pygame.image.load('assets/Bird/Bird1.png'), pygame.image.load('assets/Bird/Bird2.png')]

    def update(self, game_speed, width):
        self.x -= game_speed

        if self.x + self.FLYING[0].get_width() < 0:
            self.x = width

