import pygame

class Dino(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.RUNNING = [pygame.image.load('images/dinorun1.png'),
                        pygame.image.load('images/dinorun2.png')]

        self.DUCKING = [pygame.image.load('assets/Dino/DinoDuck1.png'),
                   pygame.image.load('assets/Dino/DinoDuck2.png')]

        self.DEAD = pygame.image.load('images/dinodead.png')

        self.image = self.RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310
        self.starting_y = 310
        self.jump_velocity = 20
        self.dino_animation_speed = 20

        self.running = True
        self.ducking = False
        self.jumping = False

    def update(self, step):

        if self.running:
            self.rect.y = 310
            self.image = self.RUNNING[(step // self.dino_animation_speed) % len(self.RUNNING)]
        elif self.jumping:
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= 1

            if self.rect.y > self.starting_y:
                self.rect.y = self.starting_y
                self.running = True
                self.jumping = False
                self.jump_velocity = 20

        else:
            self.rect.y = 340
            self.image = self.DUCKING[(step // self.dino_animation_speed) % len(self.DUCKING)]


    def input(self, keys):

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ducking = False
            self.running = False
            self.jumping = True
        elif not self.jumping:
            self.ducking = False
            self.running = True
            self.jumping = False