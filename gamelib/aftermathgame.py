import pygame
from pygame.locals import *
from gamelib.util import *
from gamelib.character import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *
from gamelib.villagemodel import *
from gamelib.aftermathworld import *


class AftermathGame(object):
    def __init__(self, surface, screen, screensize, gfx):
        self.screen = screen
        self.surface = surface
        self.screensize = screensize
        self.gfx = gfx
        #
        self.create_world()
        self.build_cast()
        self.construct_village()

    def build_cast(self):
        chars = self.world.get_characters()
        self.player = self.create_character(chars[0], self.gfx.amy)
        self.bill = self.create_character(chars[1], self.gfx.bill)
        self.cam = self.create_character(chars[2], self.gfx.cam)

    def create_character(self, character, gfx):
        return Character(gfx, self.surface, (character[2], character[3]))

    def construct_village(self):
        self.villagemodel = VillageModel()
        self.villagemodel.structures.append([8, 8, 100])
        self.villagemodel.structures.append([12, 8, 100])
        self.villagemodel.structures.append([10, 10, 100])
        self.villagemodel.structures.append([10, 9, 101])

    def create_world(self):
        self.world = AftermathWorld('world.db')
        if self.world.isNewWorld:
            self.world.create()

    def main_loop(self):

        self.update_screen()
        hmove = 0
        vmove = 0
        while True:
            for event in pygame.event.get():

                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:

                    if event.key == K_F12:
                        return

                    keystate = pygame.key.get_pressed()

                    if keystate[K_a]==1:
                        hmove = -1
                    elif keystate[K_d]==1:
                        hmove = 1

                    if keystate[K_w]==1:
                        vmove = -1
                    elif keystate[K_s]==1:
                        vmove = 1
                    if keystate[K_m]==1:
                        pygame.image.save(self.surface, "screenshot.jpeg")
                    if keystate[K_p]==1:
                        self.world.save()
                    self.player.hmove = hmove
                    self.player.vmove = vmove
                elif event.type == pygame.KEYUP:
                    keystate = pygame.key.get_pressed()

                    if keystate[K_a] == 0 and hmove < 0:
                        hmove = 0
                    if keystate[K_d] == 0 and hmove > 0:
                        hmove = 0
                    if keystate[K_w] == 0:
                        vmove = 0
                    if keystate[K_s] == 0:
                        vmove = 0

                    self.player.hmove = hmove
                    self.player.vmove = vmove
                elif event.type == ANIMEVENT:
                    self.update_screen()

    def update_screen(self):

        clear(self.surface)
        self.draw_scene()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

    def draw_scene(self):

        draw_village(self.villagemodel, self.surface, self.gfx)
        self.bill.draw()
        self.cam.draw()
        self.player.draw()

        drawText(self.surface, 20, 550, "Town Spirit : " + "Rising!")
        drawText(self.surface, 20, 580, "Time : " + "12:00")
        drawText(self.surface, 420, 550, "Amy XY : " + str(self.player.rect))
        print(self.player.rect.top)
        print(self.player.rect.left)
        print(self.player.rect.top/32)
        print(self.player.rect.left/32)
