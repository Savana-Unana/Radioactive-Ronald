import pygame
import random
import math
from pygame import mixer
from pygame.locals import *

pygame.init()
healthdonefin = 0
sped = 0
health = 1
healthbanned = health

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Scientific Blaster")

pausetheme = pygame.mixer.Sound("Spain.mp3")
syotheme = pygame.mixer.Sound('Sciotheme.mp3')
songs = []
songs.append(pausetheme)
songs.append(syotheme)


playerImage = pygame.image.load('JetRonald.png')
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Points: " + str(score_val) + '   '  + str(no_of_invaders) + '    ' + str(player_Y)+ '   '  + str(no_of_invaders) + '   '  + str(health) + '   '  + str(healthdonefin),True, (0,0,0))
    screen.blit(score, (x, y))

def game_over():
    print(score_val)
    pygame.quit()

player_X = 370
player_Y = 480
player_Xchange = 0
player_Ychange = 0


invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
invader_rect = []

sickvaderImage = []
sickvader_X = []
sickvader_Y = []
sickvader_Xchange = []
sickvader_Ychange = []
sickvader_rect = []

no_of_invaders = 3
no_of_sickvaders = 1

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('Nerd.png'))
    invaderImage.append(pygame.image.load('Dren.png'))
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
    invader_Xchange.append(0.2) # Invader speed
    invader_Ychange.append(50)

for num in range(no_of_sickvaders):
    sickvaderImage.append(pygame.image.load('NerdP.png'))
    sickvaderImage.append(pygame.image.load('Dren.png'))
    sickvader_X.append(random.randint(64, 737))
    sickvader_Y.append(random.randint(30, 180))
    sickvader_Xchange.append(0.1) # Sickvader speed
    sickvader_Ychange.append(50)

guardImage = pygame.image.load('NerdR.png')
guard_X = random.randint(50, screen_width - guardImage.get_width() - 50)
guard_Y = screen_height - guardImage.get_height() - 10
guard_Xchange = 1  # adjust speed here
guard_rect = guardImage.get_rect(topleft=(guard_X, guard_Y))

bulletImage = pygame.image.load('laser.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 1.2
bullet_state = "rest"


def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) +
                         (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))


def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def sickvader(x, y, i):
    screen.blit(sickvaderImage[i], (x, y))

def guard(x, y):
    screen.blit(guardImage, (x, y))
    guard_X += guard_Xchange
    if guard_X <= 0 or guard_X >= screen_width - guardImage.get_width():
        guard_Xchange *= -1
    guard_rect.topleft = (guard_X, y)

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"

paused = False

def pause_game():
    global paused
    paused = True



running = True
while running:


    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player_Y == 480:
                    player_Y -= 50
            if event.key == pygame.K_DOWN:
                if player_Y == 430:
                    player_Y += 50
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
                playerImage = pygame.image.load('JetRonald.png')
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
                playerImage = pygame.image.load('JetRonald_right.png')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game()
            if event.key == pygame.K_SPACE:

                if bullet_state is "rest":
                    bullet_X = player_X
                    bullet(bullet_X, bullet_Y)
                    bullet_sound = mixer.Sound('jump.mp3')
                    bullet_sound.play()
        if event.type == pygame.KEYUP:
            player_Xchange = 0

    player_X += player_Xchange
    player_Y += player_Ychange

    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]

    for i in range(no_of_sickvaders):  # Add sickvaders to the game loop
        sickvaderImage.append(pygame.image.load('NerdP.png'))
        sickvader_X.append(random.randint(64, 737))
        sickvader_Y.append(random.randint(30, 180))
        sickvader_Xchange.append(0.9)  # Sickvader speed
        sickvader_Ychange.append(50)

    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state is "fire":
        bullet(bullet_X, bullet_Y)

        bullet_Y -= bullet_Ychange

    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]

        # Update sickvader positions
    for i in range(no_of_sickvaders):
        sickvader_X[i] += sickvader_Xchange[i]

    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state is "fire":
        bullet(bullet_X, bullet_Y)

        bullet_Y -= bullet_Ychange

        # Invader collision
    for i in range(no_of_invaders):

        if invader_Y[i] >= 450:
            if abs(player_X - invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    explosion_sound = mixer.Sound('jet.mp3')
                    explosion_sound.play()
                game_over()
                break

        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]
        collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])

        if collision:

            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1


        invader(invader_X[i], invader_Y[i], i)

        # Sickvader collision (similar logic as invader collision)
    for i in range(no_of_sickvaders):

        if sickvader_Y[i] >= 450:
            if abs(player_X - sickvader_X[i]) < 80:
                for j in range(no_of_sickvaders):
                    sickvader_Y[j] = 2000
                    explosion_sound = mixer.Sound('jet.mp3')
                    explosion_sound.play()
                game_over()
                break

        if sickvader_X[i] >= 735 or sickvader_X[i] <= 0:
            sickvader_Xchange[i] *= -1
            sickvader_Y[i] += sickvader_Ychange[i]
        collision = isCollision(bullet_X, sickvader_X[i],
                                bullet_Y, sickvader_Y[i])

        if collision:
            health -= 1
            healthdonefin += 1
            bullet_Y = 600
            bullet_state = "rest"

        if health == 0:
            score_val += 3
            sickvader_X[i] = random.randint(64, 736)
            sickvader_Y[i] = random.randint(30, 200)
            sickvader_Xchange[i] *= -1
            health = healthbanned
            health *= 2
            healthbanned = health

        sickvader(sickvader_X[i], sickvader_Y[i], i)

    pressed = pygame.key.get_pressed()
    if player_X <= 16:
        player_X = 16;
    elif player_X >= 750:
        player_X = 750

#for score_val in range(score_val+1):
    #invader_Xchange[0] = sped
    #invader_Xchange[0] = int(score_val)/10 + sped

    if score_val == 10000:
        game_over()

    while paused:
        pygame.mixer.Sound.stop(songs[1])
        sesong = 3
        sesong = random.randint(0, 2)
        if sesong == 0:
            pygame.mixer.Sound.play(songs[0])
        if sesong == 1:
            pygame.mixer.Sound.stop(songs[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.Sound.stop(songs[0])
                    paused = False
    else:
        pygame.mixer.Sound.play(songs[1])
    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update()
