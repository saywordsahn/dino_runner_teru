import pgzrun
from enum import Enum
import random as rand

WIDTH = 1100
HEIGHT = 600
WHITE = (255, 255, 255)
GRAVITY = 100.0
STARTING_SPEED = 9
SPEED_INCREASE_AMOUNT = 0.3
JUMP_POWER = -30.0
DINO_STARTING_Y = 425
DINO_DUCKING_Y = 450


class PlayerState(Enum):
    RUNNING = 1
    JUMPING = 2
    DUCKING = 3
    DEAD = 4

class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2

RUNNING = ['dinorun1', 'dinorun2']
DUCKING = ['dinoduck1', 'dinoduck2']
FLAPPING = ['bird1', 'bird2']

# todo: ducking
# todo: different obstacle types
# todo: OBJECTS!
# todo: score - high score
# todo: score - fix orientation
# todo: score - font
# todo: start screen


# candidates for next
# 1. power up jumping game
# 2. hypersnake
# 3. clicker game


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


#############
# CLOUDS
#############
clouds = []
cloud_speed = 2.0
cloud_min_y = 140
cloud_max_y = 400
cloud_cooldown = 2.0
cloud_last_spawned_time = 0.0


time = 0
last_speed_increase = 0
score = 0
last_score_update = 0
game_state = GameState.PLAYING
speed = STARTING_SPEED
track_x = 0
track2_x = 2404
track_y = 450

reset_button = Actor('reset', (WIDTH / 2 - 75 / 2, HEIGHT / 2))


def reset_dino():
    dino.y = DINO_STARTING_Y
    dino.animation_length = 0.2
    dino.last_animation_changed = 0.0
    dino.frame_count = 0
    dino.state = PlayerState.RUNNING
    dino.jump_velocity = 0.0

def reset():
    global game_state, clouds, speed, score

    game_state = GameState.PLAYING
    reset_dino()
    cactus.left = WIDTH
    clouds = []
    speed = STARTING_SPEED
    score = 0


def draw():

    screen.fill(WHITE)
    screen.blit('track', (track_x, track_y))
    screen.blit('track', (track2_x, track_y))
    screen.draw.text(str(score), (1000, 30), color='gray', fontname='dinofont', fontsize=32)

    for cloud in clouds:
        cloud.draw()

    dino.draw()
    bird.draw()
    cactus.draw()



    if game_state == GameState.GAME_OVER:
        screen.blit('gameover', (WIDTH / 2 - 386 / 2, HEIGHT / 2 - 100))
        reset_button.draw()

        # screen.draw.text("GAME OVER", (20, 100), fontsize=60, color='red')


def update_track():
    global track_x, track2_x

    if game_state == GameState.PLAYING:
        # update track position
        track_x -= speed
        track2_x -= speed

        if track_x < -2404:
            track_x = 2404

        if track2_x < -2404:
            track2_x = 2404



def handle_collision():
    global game_state

    if dino.colliderect(cactus):
        change_state(PlayerState.DEAD)
        game_state = GameState.GAME_OVER


def change_state(new_state):
    dino.state = new_state

    if new_state == PlayerState.DUCKING:
        dino.image = 'dinoduck1'
        dino.y = DINO_DUCKING_Y
    elif new_state == PlayerState.RUNNING:
        dino.image = 'dinorun1'
        dino.y = DINO_STARTING_Y
    elif new_state == PlayerState.JUMPING:
        dino.jump_velocity = JUMP_POWER
    else:
        dino.image = 'dinodead'



def update_dino(time, dt):

    if dino.state == PlayerState.RUNNING:

        if time - dino.last_animation_changed > dino.animation_length:
            dino.frame_count += 1
            dino.image = RUNNING[dino.frame_count % len(RUNNING)]
            dino.last_animation_changed = time

        if keyboard.SPACE or keyboard.UP or keyboard.W:
            change_state(PlayerState.JUMPING)

        if keyboard.S or keyboard.DOWN:
            change_state(PlayerState.DUCKING)

    elif dino.state == PlayerState.JUMPING:
        dino.jump_velocity += GRAVITY * dt
        dino.y += dino.jump_velocity

        if dino.y >= DINO_STARTING_Y:
            change_state(PlayerState.RUNNING)
    else:

        if time - dino.last_animation_changed > dino.animation_length:
            dino.frame_count += 1
            dino.image = DUCKING[dino.frame_count % len(DUCKING)]
            dino.last_animation_changed = time

        if not (keyboard.S or keyboard.DOWN):
            change_state(PlayerState.RUNNING)







def update_clouds(time):
    global cloud_last_spawned_time

    if game_state == GameState.PLAYING:

        # spawn clouds
        if time - cloud_last_spawned_time > cloud_cooldown:
            clouds.append(Actor('cloud', (WIDTH, rand.randint(cloud_min_y, cloud_max_y))))
            cloud_last_spawned_time = time

        # move cloud
        for cloud in clouds:
            cloud.x -= cloud_speed

def update_cactus():

    if game_state == GameState.PLAYING:
        cactus.x -= speed

        if cactus.x < 0:
            cactus.x = WIDTH

def update(dt):
    global time, speed, last_speed_increase, score, last_score_update

    time += dt

    if time - last_speed_increase >= 1.0:
        speed += SPEED_INCREASE_AMOUNT
        last_speed_increase = time

    if game_state == GameState.PLAYING and time - last_score_update > 0.1:
        score += 1
        last_score_update = time

    update_track()
    update_dino(time, dt)
    update_clouds(time)
    # update_cactus()
    handle_collision()


    if time - bird.last_animation_changed > bird.animation_length:
        bird.frame_count += 1
        bird.image = FLAPPING[bird.frame_count % len(RUNNING)]
        bird.last_animation_changed = time

def on_mouse_down(pos):

    if reset_button.collidepoint(pos) and game_state == GameState.GAME_OVER:
        reset()




pgzrun.go()