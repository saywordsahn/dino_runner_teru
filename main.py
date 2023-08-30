import pygame

class Bird:

    def __init__(self):

        self.image = FLAPPING[0]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = 290

    def update(self):
        self.image = FLAPPING[(step // bird_animation_speed) % len(RUNNING)]

        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.rect.x = WIDTH



class Dino:

    def __init__(self):

        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310
        self.jump_velocity = 20

        self.RUNNING = True
        self.DUCKING = False
        self.JUMPING = False



    def update(self):

        if self.RUNNING:
            self.rect.y = 310
            self.image = RUNNING[(step // dino_animation_speed) % len(RUNNING)]
        elif self.JUMPING:
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= 1
        else:
            self.rect.y = 340
            self.image = DUCKING[(step // dino_animation_speed) % len(DUCKING)]




    def input(self, keys):

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.DUCKING = True
            self.RUNNING = False
            self.JUMPING = False
        elif keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.DUCKING = False
            self.RUNNING = False
            self.JUMPING = True
        else:
            self.DUCKING = False
            self.RUNNING = True
            self.JUMPING = False


pygame.init()

WIDTH = 1100
HEIGHT = 600
fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RUNNING = [pygame.image.load('assets/Dino/DinoRun1.png'),
           pygame.image.load('assets/Dino/DinoRun2.png')]

DUCKING = [pygame.image.load('assets/Dino/DinoDuck1.png'),
           pygame.image.load('assets/Dino/DinoDuck2.png')]

FLAPPING = [pygame.image.load('assets/Bird/Bird1.png'),
            pygame.image.load('assets/Bird/Bird2.png')]

TRACK = pygame.image.load('assets/Other/Track.png')

# animation speeds
dino_animation_speed = 20
bird_animation_speed = 20


# objects
dino = Dino()
bird = Bird()

x_pos_bg = 0
y_pos_bg = 380

step = 0
game_speed = 5

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
    dino.update()
    bird.update()


    # draw
    screen.fill(0)
    background()

    screen.blit(dino.image, (dino.rect.x, dino.rect.y))
    screen.blit(bird.image, (bird.rect.x, bird.rect.y))

    pygame.display.update()