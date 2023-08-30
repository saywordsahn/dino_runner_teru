import pygame

class Dino:

    def __init__(self):
        self.x = 80
        self.y = 310
        self.is_running = True
        self.RUNNING = [pygame.image.load('assets/Dino/DinoRun1.png'), pygame.image.load('assets/Dino/DinoRun2.png')]
        self.DUCKING = [pygame.image.load('assets/Dino/DinoDuck1.png'), pygame.image.load('assets/Dino/DinoDuck2.png')]
