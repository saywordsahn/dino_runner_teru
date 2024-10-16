import pygame

class Bird(pygame.sprite.Sprite):

    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)
        self.FLAPPING = [pygame.image.load('images/bird1.png'),
                         pygame.image.load('images/bird2.png')]
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