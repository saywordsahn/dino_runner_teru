import pygame

class Cactus(pygame.sprite.Sprite):

    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/Cactus/LargeCactus3.png')
        self.rect = self.image.get_rect()
        self.width = width
        self.rect.x = width / 2
        self.rect.y = 300
        self.bird_animation_speed = 20

    def update(self, step, game_speed):

        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.rect.x = self.width