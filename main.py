import pygame
from dino import Dino
from bird import Bird
from cactus import Cactus


pygame.init()

WIDTH = 1100
HEIGHT = 600
fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

TRACK = pygame.image.load('images/track.png')

# animation speeds
bird_animation_speed = 20


# objects
dino = Dino()
player_group = pygame.sprite.Group()
player_group.add(dino)

bird = Bird(WIDTH)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(bird)

cactus = Cactus(WIDTH)
obstacle_group.add(cactus)

x_pos_bg = 0
y_pos_bg = 380

step = 0
game_speed = 10
game_over = False

def background():
    global x_pos_bg, y_pos_bg
    image_width = TRACK.get_width()
    screen.blit(TRACK, (x_pos_bg, y_pos_bg))
    screen.blit(TRACK, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        screen.blit(TRACK, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed

# main game loop
while True:
    step += 1
    time = clock.tick(fps)
    # input
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed()

    dino.input(keys)

    # update
    dino.update(step)
    bird.update(step, game_speed)
    cactus.update(step, game_speed)

    # check for collision
    if dino.rect.colliderect(bird.rect):
        # change the dino's image to dinodead.png
        dino.image = dino.DEAD
        game_over = True



    # draw
    screen.fill(0)
    background()

    obstacle_group.draw(screen)
    player_group.draw(screen)

    pygame.display.update()