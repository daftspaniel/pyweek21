import pygame
from pygame.locals import *
from gamelib.util import *
from gamelib.player import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *
from gamelib.villagemodel import *


class AftermathGame(object):
    def __init__(self, surface, screen, screensize, gfx):
        self.screen = screen
        self.surface = surface
        self.screensize = screensize
        self.gfx = gfx
        self.build_cast()
        self.construct_village()

    def build_cast(self):
        self.player = Player(self.gfx.amy, self.surface, (10, 10))
        self.bill = Player(self.gfx.bill, self.surface, (6, 8))
        self.cam = Player(self.gfx.cam, self.surface, (7, 8))

    def construct_village(self):
        self.villagemodel = VillageModel()
        self.villagemodel.structures.append([8, 8, 100])
        self.villagemodel.structures.append([12, 8, 100])
        self.villagemodel.structures.append([10, 10, 100])
        self.villagemodel.structures.append([10, 9, 101])

    def new_world(self):
        pass

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
