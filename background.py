import pygame

class Background:

    def __init__(self):
        self.image = pygame.image.load('assets/Other/Track.png')
        self.x = 0
        self.y = 380

    def update(self, game_speed, width):
        self.x -= game_speed
        if self.x + self.image.get_width() < 0:
            self.x = width