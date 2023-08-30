import pygame
from dino import Dino
from bird import Bird
from background import Background



pygame.init()
width = 1100
height = 600
fps = 60
game_speed = 6

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# dinosaur
dino = Dino()

# bird x = 400, y = 290
bird = Bird()

bg = Background()

LargeCactus = [pygame.image.load('assets/Cactus/LargeCactus1.png'), pygame.image.load('assets/Cactus/LargeCactus2.png'),
               pygame.image.load('assets/Cactus/LargeCactus3.png')]
SmallCactus = [pygame.image.load('assets/Cactus/SmallCactus1.png'), pygame.image.load('assets/Cactus/SmallCactus2.png'),
               pygame.image.load('assets/Cactus/SmallCactus3.png')]

frame_count = 0

while True:

    time = clock.tick(fps)
    frame_count += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] == True:
        dino.is_running = False
    else:
        dino.is_running = True

    # update
    bird.update(game_speed, width)
    bg.update(game_speed, width)



    # draw
    screen.fill((255, 255, 255))
    if dino.is_running:
        screen.blit(dino.RUNNING[(frame_count // 10) % len(dino.RUNNING)], (dino.x, dino.y))
    else:
        screen.blit(dino.DUCKING[(frame_count // 10) % len(dino.DUCKING)], (dino.x, dino.y + 40))

    screen.blit(bird.FLYING[(frame_count // 20) % len(bird.FLYING)], (bird.x, bird.y))
    screen.blit(bg.image, (bg.x, bg.y))

    pygame.display.update()
