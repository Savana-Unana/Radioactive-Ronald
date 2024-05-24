import pygame
import subprocess
import random
from pygame.locals import *

pygame.init()


pygame.display.set_caption("Choose Your Battle")
menutheme = pygame.mixer.Sound("Menu.mp3")
secrettheme = pygame.mixer.Sound("SecretMenu.mp3")
songs = []
songs.append(menutheme)
songs.append(secrettheme)
global mute
pressed = pygame.key.get_pressed()
y = random.randint(0, 1)
if y == 0:
    pygame.mixer.Sound.play(songs[0])
    y = 2
if y == 1:
    pygame.mixer.Sound.play(songs[1])
    y = 3


screen = pygame.display.set_mode((500, 500))

def show_score(x, y):
    score = font.render(str())
    screen.blit(score, (x, y))

def mute():
    pressed = pygame.key.get_pressed()
    global muted
    if pressed[K_m]:
        menutheme.set_volume(0)
    if pressed[K_u]:
        menutheme.set_volume(1.0)


# Function to draw a button
def draw_button(screen, color, x, y, width, height, text, font):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surface, text_rect)
    return text_rect


# Function to check if a point (mouse click) is within a rectangle
def point_inside_rect(x, y, rect):
    return rect.left < x < rect.right and rect.top < y < rect.bottom


# Main game loop
running = True
button_rect = draw_button(screen, (0, 0, 255), 200, 200, 100, 50, "load retart12", pygame.font.Font(None, 36))
button_rect1 = draw_button(screen, (0, 0, 255), 200, 400, 100, 50, "Ariel is ginger", pygame.font.Font(None, 36))
button_rect2 = draw_button(screen, (0, 0, 255), 200, 0, 100, 50, "Science Invaders", pygame.font.Font(None, 36))
button_rect3 = draw_button(screen, (0, 0, 255), 200, 300, 100, 50, "Sus", pygame.font.Font(None, 36))


pygame.display.flip()

subproc_launched = False


while running:
    mute()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and not subproc_launched:
            if point_inside_rect(*event.pos, button_rect):
                running = False
                subprocess.Popen(["python", "retart12.py"])
                subproc_launched = True
            if point_inside_rect(*event.pos, button_rect1):
                running = False
                subprocess.Popen(["python", "redo.py"])
                subproc_launched = True
            if point_inside_rect(*event.pos, button_rect2):
                running = False
                subprocess.Popen(["python", "undo.py"])
                subproc_launched = True
            if point_inside_rect(*event.pos, button_rect3):
                running = False
                subprocess.Popen(["python", "LK-99_version01.py"])
                subproc_launched = True
while running is False:
    pygame.quit()





