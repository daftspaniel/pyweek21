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
        self.player = Player(self.gfx.amy, self.surface, (10, 10))
        self.villagemodel = VillageModel()

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
        self.player.draw()