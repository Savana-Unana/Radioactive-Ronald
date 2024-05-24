import pygame
from pygame.locals import *
from save import SaveLoadSystem


pygame.init()
screen = pygame.display.set_mode((500, 500))
anglechange = 0
global healthpoint
healthpoint = 4
global fricktion
fricktion = 1.05
global rollfaceright
rollfaceright = 0
global boxdrop
boxdrop = 0
global jetpower
jetpower = 100
invdo = False
invstart = False
invframes = 10000
global spiketrap
spiketrap = False

pygame.display.set_caption("The Tutorial Area")

jumpsound = pygame.mixer.Sound("Jump.mp3")
jetsound = pygame.mixer.Sound("Jet.mp3")
syotheme = pygame.mixer.Sound("Syotheme.mp3")
hurtsound = pygame.mixer.Sound("Hurt.mp3")
wawasound = pygame.mixer.Sound("Wawawawawa.mp3")
yowsound = pygame.mixer.Sound("Yowchee.mp3")

#gingersound = pygame.mixer.Sound("Ginger.mp3")
pgruntsound = pygame.mixer.Sound("PGrunt.mp3")
sfx = []
songs = []
sfx.append(jumpsound)
#sfx.append(gingersound)
sfx.append(jetsound)
sfx.append(hurtsound)
sfx.append(pgruntsound)
sfx.append(wawasound)
sfx.append(yowsound)
songs.append(syotheme)
x=0
global muted


DISPLAYSURF = pygame.display.set_mode((800, 600))




def mute():
    pressed = pygame.key.get_pressed()
    global muted
    if pressed[K_m]:
        jumpsound.set_volume(0)
        hurtsound.set_volume(0)
        jetsound.set_volume(0)
        pgruntsound.set_volume(0)
        wawasound.set_volume(0)
        yowsound.set_volume(0)
        syotheme.set_volume(0)

        syotheme.set_volume(0)
    if pressed[K_u]:
        jumpsound.set_volume(1.0)
        hurtsound.set_volume(1.0)
        jetsound.set_volume(1.0)
        pgruntsound.set_volume(1.0)
        wawasound.set_volume(1.0)
        yowsound.set_volume(1.0)
        syotheme.set_volume(1.0)



def draw_jetpower_bar(surf, x, y, fuel):
    bar_width = 100
    bar_height = 10
    fill = (fuel / 100) * bar_width

    outline_rect = pygame.Rect(x, y, bar_width, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)

    GREEN = 0, 255, 255
    WHITE = 255, 255, 255

    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_health_bar(surf, x, y, health):
    if healthpoint >= 4:
        healthImage  = pygame.image.load('health5.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint == 3:
        healthImage  = pygame.image.load('health4.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint == 2:
        healthImage  = pygame.image.load('health3.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint == 1:
        healthImage  = pygame.image.load('health2.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint == 0:
        healthImage  = pygame.image.load('health1.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint == -1:
        healthImage = pygame.image.load('health0.png')
        screen.blit(healthImage, [50, 50])
    if healthpoint < -1:
        healthImage = pygame.image.load('health0.png')
        screen.blit(healthImage, [50, 50])
        pygame.mixer.Sound.play(sfx[4])
        pygame.time.wait(3000)
        event.type = QUIT
        print('')


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.move = pygame.math.Vector2()
        self.angle = 0
        self.can_jump = True
        self.jump_image = None
        self.left = False
        self.right = False

        self.ivspritesr = []
        self.ivspritesl = []
        self.ivspritesl.append(pygame.image.load('ivRonald0.png'))
        self.ivspritesl.append(pygame.image.load('ivRonald1.png'))
        self.ivspritesr.append(pygame.image.load('ivRonald_right0.png'))
        self.ivspritesr.append(pygame.image.load('ivRonald_right1.png'))
        self.current_ivsprite = 0
        try:
            self.original_image = pygame.image.load('lessfatRonald.png')
        except:
            self.original_image = pygame.Surface((20, 20))
            self.original_image.fill((255, 0, 0))

        self.image = self.original_image
        self.rect = self.image.get_rect(midbottom=(round(self.pos.x), round(self.pos.y)))



    def update(self, time_passed):
        pressed = pygame.key.get_pressed()
        self.move.x *= fricktion + 0.08


        if self.can_jump:
            if pressed[K_LEFT]:
                self.original_image = pygame.image.load('lessfatRonald.png')
                self.move.x -= 25
                self.left = True
                self.right = False
                if pressed[K_LSHIFT]:
                    self.angle += 2
                    self.move.x -= 45
                if not pressed[K_LSHIFT]:
                    self.angle = 0
            if pressed[K_RIGHT]:
                self.original_image = pygame.image.load('lessfatRonald_right0.png')
                self.move.x += 25
                self.left = False
                self.right = True
                if pressed[K_LSHIFT]:
                    self.angle -= 2
                    self.move.x += 45
                if not pressed[K_LSHIFT]:
                    self.angle = 0

        else:
            if pressed[K_LEFT]:
                self.original_image = pygame.image.load('lessfatRonald.png')
                self.move.x -= 25
                self.left = True
                self.right = False
                if pressed[K_LSHIFT]:
                    self.move.x -= 45
                if not pressed[K_LSHIFT]:
                    self.angle = 0
            if pressed[K_RIGHT]:
                self.original_image = pygame.image.load('lessfatRonald_right0.png')
                self.move.x += 25
                self.left = False
                self.right = True
                if pressed[K_LSHIFT]:
                    self.move.x += 45
                if not pressed[K_LSHIFT]:
                    self.angle = 0

        global anglechange
        global healthpoint
        if pressed[K_v] and pressed[K_o]:
            anglechange = 1
        if pressed[K_z] and pressed[K_o]:
            anglechange = 2
        if pressed[K_x] and pressed[K_o]:
            anglechange = 3
        if pressed[K_z] and pressed[K_p]:
            anglechange = 0
        if pressed[K_x] and pressed[K_p]:
            anglechange = 7
        if pressed[K_d] and pressed[K_k]:
            healthpoint -= 1
            pygame.mixer.Sound.play(sfx[2])
        if anglechange == 0:

            if not pressed[K_LEFT] or pressed[K_LSHIFT]:
                self.angle = 0
            if not pressed[K_RIGHT] or pressed[K_LSHIFT]:
                self.angle = 0

        if anglechange == 2:
            self.can_jump = False
            if True:
                if pressed[K_LEFT]:
                    self.original_image = pygame.image.load('ballRonald.png')
                    if pressed[K_LSHIFT]:
                        self.angle += 20
                        self.move.x -= 10
                    if not pressed[K_LSHIFT]:
                        self.angle += 10
                        self.move.x -= 5
                    global rollfaceright
                    rollfaceright = 2
                if pressed[K_RIGHT]:
                    self.original_image = pygame.image.load('ballRonald_right.png')
                    if pressed[K_LSHIFT]:
                        self.angle -= 20
                        self.move.x += 10
                    if not pressed[K_LSHIFT]:
                        self.angle -= 10
                        self.move.x += 5
                    rollfaceright = 1
                else:
                    if pressed[K_RIGHT] or not pressed[K_LEFT]:
                        if rollfaceright == 1:
                            self.original_image = pygame.image.load('Ronaldroll_right.png')
                            self.angle = 0
                        if rollfaceright == 2:
                            self.original_image = pygame.image.load('Ronaldroll.png')
                            self.angle = 0



        if anglechange == 3:
            speed_modifier = 3
            if True:
                if pressed[K_LEFT]:
                    self.original_image = pygame.image.load('lessfatRonald.png')
                    self.angle = 0
                    self.move.x -= 20
                    self.left = True
                    self.right = False
                    if True:
                        self.move.x += speed_modifier * (fricktion + 0.8)
                if pressed[K_RIGHT]:
                    self.angle = 0
                    self.original_image = pygame.image.load('lessfatRonald_right0.png')
                    self.move.x += 20
                    self.left = False
                    self.right = True
                    if True:
                        self.move.x -= speed_modifier * (fricktion + 0.8)

        if anglechange == 4:
            if True:
                self.can_jump = False
                if pressed[K_LEFT]:
                    self.angle = 0
                    self.original_image = pygame.image.load('BoxRonald.png')
                    self.left = True
                    self.right = False
                if pressed[K_RIGHT]:
                    self.angle = 0
                    self.original_image = pygame.image.load('BoxRonald_right.png')
                    self.left = False
                    self.right = True
                if pressed[K_e]:
                    global boxdrop
                    if self.left == True:
                        self.original_image = pygame.image.load('BoxRonald.png')
                    if self.right == False:
                        self.original_image = pygame.image.load('BoxRonald_right.png')
                    boxdrop = 1

        if anglechange == 5:
            global jetpower
            if True:
                self.can_jump = True
                if pressed[K_LEFT]:
                    self.angle = 0
                    self.original_image = pygame.image.load('JetRonald.png')
                    self.left = True
                    self.right = False
                if pressed[K_RIGHT]:
                    self.angle = 0
                    self.original_image = pygame.image.load('JetRonald_right.png')
                    self.left = False
                    self.right = True
                if pressed[K_e]:
                    if self.left == True:
                        self.original_image = pygame.image.load('JetRonald.png')
                    if self.right == False:
                        self.original_image = pygame.image.load('JetRonald_right.png')
                    boxdrop = 1
        global invstart
        global invdo
        global invframes
        if anglechange == 6:
            global iv
            if True:
                self.current_ivsprite += 1
                if self.current_ivsprite >= len(self.ivspritesl):
                    self.current_ivsprite = 0
                if self.current_ivsprite >= len(self.ivspritesr):
                    self.current_ivsprite = 0
                if pressed[K_LEFT]:
                    self.image = self.ivspritesl[self.current_ivsprite]
                    self.angle = 0
                    self.left = True
                    self.right = False
                if pressed[K_RIGHT]:
                    self.image = self.ivspritesr[self.current_ivsprite]
                    self.angle = 0
                    self.left = False
                    self.right = True
                if invstart == True:
                    healthpoint -= 1
                    invstart = False

                if invstart == True:
                    invframes -= 1
                    pygame.time.wait(1)
                    if invframes == 0:
                        invdo = False
                        anglechange = 3
                        invframes = 10000

        if anglechange != 6:
            invdo = False

        if anglechange == 7:
            self.can_jump = True




        if boxdrop == 1:
            anglechange = 3
            companions.original_image = pygame.image.load("Companion.png")

        if pressed[K_UP] and self.can_jump:
            if pressed[K_LEFT]:
                self.jump_image = pygame.image.load('jumpinRonald.png')
            if pressed[K_RIGHT]:
                self.jump_image = pygame.image.load('jumpinRonald_right.png')
            if pressed[K_g]:
                pygame.mixer.Sound.play(sfx[5])
            if anglechange == 5:
                pygame.mixer.Sound.play(sfx[1])
                jetpower -= 10
                if jetpower <= 0:
                    anglechange = 0
                if pressed[K_LEFT]:
                    self.jump_image = pygame.image.load('flyRonald.png')
                if pressed[K_RIGHT]:
                    self.jump_image = pygame.image.load('flyRonald_right.png')
            else:
                pygame.mixer.Sound.play(sfx[0])


            self.can_jump = False
            self.move.y = -1000

        self.pos = self.pos + self.move * time_passed
        self.move.x *= 0.8
        self.move.y += 5000 * time_passed

        if self.pos.y > 600:
            self.pos.y = 600
            self.can_jump = True

        if self.jump_image is not None:
            self.image = self.jump_image
        else:
            self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect = self.image.get_rect(midbottom=(round(self.pos.x), round(self.pos.y)))

        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.centerx
        if self.rect.right > 800:
            self.rect.right = 800
            self.pos.x = self.rect.centerx
        if self.pos.y >= 600:
            self.pos.y = 600
            self.can_jump = True
            self.jump_image = None



class Companion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("Companion.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")

    def collide_with_player(self, player):
        if player.rect.colliderect(self.rect):
            if player.rect.bottom != self.rect.top:
                pressed = pygame.key.get_pressed()
                #player.pos.x +=20
                if pressed[K_SPACE]:
                    self.image = pygame.image.load("GhostRonald.png")
                    global anglechange
                    anglechange = 4
                    pygame.mixer.Sound.play(sfx[3])

class Jetpack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("Pack.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")

    def collide_with_player(self, player):
        if player.rect.colliderect(self.rect):
            if player.rect.bottom != self.rect.top:
                pressed = pygame.key.get_pressed()
                #player.pos.x +=20
                if pressed[K_SPACE]:
                    self.image = pygame.image.load("GhostRonald.png")
                    global anglechange
                    anglechange = 5
                    global jetpower
                    jetpower = 100

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("Door.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")


    def collide_with_player(self, player):
        if player.rect.colliderect(self.rect):
            if player.rect.bottom != self.rect.top:
                pressed = pygame.key.get_pressed()
                if pressed[K_SPACE]:
                    self.image = pygame.image.load("GhostRonald.png")

class EvilDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("Door.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")

    def collide_with_player(self, player):
        global spiketrap
        if player.rect.colliderect(self.rect):
            if player.rect.bottom != self.rect.top:
                pressed = pygame.key.get_pressed()
                if pressed[K_SPACE]:
                    self.image = pygame.image.load("GhostRonald.png")
                    spiketrap = True



class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")


class Bartly(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #%$
        global spiketrap
        super().__init__()
        self.image = pygame.image.load("bartly.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        if spiketrap == True:
            self.image = pygame.image.load("GhostRonald.png")

    def collide_with_player(self, player):
        global healthpoint
        global anglechange
        if player.rect.colliderect(self.rect):
            if player.rect.bottom != self.rect.top:
                global invdo
                global invstart
                if not invdo:
                    invdo = True
                    invstart = True
                    if anglechange != 6:
                        anglechange = 6
                        pygame.mixer.Sound.play(sfx[2])
                    else:
                        pass
                else:
                    pass

companions = pygame.sprite.Group()
companion = Companion(0, 500)
companions.add(companion)
packs = pygame.sprite.Group()
pack = Jetpack(200, 500)
packs.add(pack)
doors = pygame.sprite.Group()
door = Door(400, 500)
doors.add(door)
evildoors = pygame.sprite.Group()
evildoor = EvilDoor(400, 300)
evildoors.add(evildoor)
lasers = pygame.sprite.Group()
laser = Jetpack(200, 500)
lasers.add(laser)
bartlys = pygame.sprite.Group()
bartly = Bartly(600, 500)
bartlys.add(bartly)
player = Player(400, 600)
allSprites = pygame.sprite.Group(player)



clock = pygame.time.Clock()
saveloadmanager = SaveLoadSystem(".save", "save_data")
entities, number = saveloadmanager.load_game_data(["entities", "number"], [[], 1])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            saveloadmanager.save_game_data([entities, number], ["entities", "number"])
            pygame.quit()
            exit()

    #if event.type == pygame.MOUSEBUTTONDOWN:
       #if player_rect.collidepoint(event.pos):

    companion.collide_with_player(player)
    pack.collide_with_player(player)
    door.collide_with_player(player)
    evildoor.collide_with_player(player)
    laser.collide_with_player(player)
    bartly.collide_with_player(player)

    if spiketrap == True:
        pygame.display.set_caption("Bad Door")

    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    print(healthpoint)


    allSprites.update(clock.tick(60) / 1000)
    screen.fill((220, 220, 255))
    companions.update()
    companions.draw(screen)
    packs.update()
    packs.draw(screen)
    laser.update()
    lasers.draw(screen)
    door.update()
    doors.draw(screen)
    evildoor.update()
    evildoors.draw(screen)
    bartly.update()
    bartlys.draw(screen)
    mute()
    draw_jetpower_bar(screen, 10, 10, jetpower)
    draw_health_bar(screen, 10, 10, healthpoint)
    allSprites.draw(screen)
    pygame.display.flip()

    if x == 0:
        #pygame.mixer.Sound.play(songs[0])
        x=1
