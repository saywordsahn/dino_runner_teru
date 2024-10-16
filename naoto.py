import pgzrun
from enum import Enum

WIDTH = 1100
HEIGHT = 600
WHITE = (255, 255, 255)
GRAVITY = 160.0
DINO_STARTING_Y = 425

class PlayerState(Enum):
    RUNNING = 1
    JUMPING = 2
    DUCKING = 3
    DEAD = 4

RUNNING = ['dinorun1', 'dinorun2']
FLAPPING = ['bird1', 'bird2']


# class Player(Actor):
#
#     def __init__(self):
#         super().__init__('dinorun1')
#         self.RUNNING = ['dinorun1', 'dinorun2']
#         self.x = 90
#         self.y = 425


cactus = Actor('smallcactus2', (WIDTH / 2, 438))


bird = Actor('bird1', (WIDTH / 2, HEIGHT / 2))
bird.animation_length = 0.4
bird.last_animation_changed = 0.0
bird.frame_count = 0


dino = Actor('dinorun1', (90, DINO_STARTING_Y))
dino.animation_length = 0.2
dino.last_animation_changed = 0.0
dino.frame_count = 0
dino.state = PlayerState.RUNNING
dino.jump_velocity = 0.0


time = 0
speed = 9
track_x = 0
track2_x = 2404
track_y = 450


def draw():
    screen.fill(WHITE)
    screen.blit('track', (track_x, track_y))
    screen.blit('track', (track2_x, track_y))
    dino.draw()
    bird.draw()
    cactus.draw()

def update_track():
    global track_x, track2_x
    # update track position
    track_x -= speed
    track2_x -= speed

    if track_x < -2404:
        track_x = 2404

    if track2_x < -2404:
        track2_x = 2404

def update_dino(time, dt):

    if dino.state == PlayerState.RUNNING:

        if time - dino.last_animation_changed > dino.animation_length:
            dino.frame_count += 1
            dino.image = RUNNING[dino.frame_count % len(RUNNING)]
            dino.last_animation_changed = time

        if keyboard.SPACE:
            dino.state = PlayerState.JUMPING
            dino.jump_velocity = -40.0

    else:
        dino.jump_velocity += GRAVITY * dt
        dino.y += dino.jump_velocity

        if dino.y >= DINO_STARTING_Y:
            dino.y = DINO_STARTING_Y
            dino.state = PlayerState.RUNNING









def update(dt):
    global time

    time += dt

    update_track()
    update_dino(time, dt)


    if time - bird.last_animation_changed > bird.animation_length:
        bird.frame_count += 1
        bird.image = FLAPPING[bird.frame_count % len(RUNNING)]
        bird.last_animation_changed = time

    cactus.x -= speed

    if cactus.x < 0:
        cactus.x = WIDTH

pgzrun.go()