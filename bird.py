import pygame

class Bird:

    def __init__(self, width):

        self.FLAPPING = [pygame.image.load('assets/Bird/Bird1.png'),
                    pygame.image.load('assets/Bird/Bird2.png')]
        self.image = self.FLAPPING[0]
        self.rect = self.image.get_rect()
        self.width = width
        self.rect.x = width
        self.rect.y = 290
        self.bird_animation_speed = 20

    def update(self, step, game_speed):
        self.image = self.FLAPPING[(step // self.bird_animation_speed) % len(self.FLAPPING)]

        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.rect.x = self.width