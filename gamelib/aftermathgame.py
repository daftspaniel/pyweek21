import pygame
from pygame.locals import *
from gamelib.util import *
from gamelib.player import *


class AftermathGame(object):
    def __init__(self, surface, screen, screensize, gfx):
        self.screen = screen
        self.surface = surface
        self.screensize = screensize
        self.gfx = gfx
        self.player = Player(self.gfx.amy, self.surface, (10, 10))

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

        self.surface.fill(pygame.Color("black"))

        self.draw_scene()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

    def draw_scene(self):

        self.draw_village()

    def draw_village(self):
        for x in range(0, 25):
            for y in range(0, 24):
                p = Rect(x * 32, y * 32, 32, 32)
                self.surface.blit(self.gfx.grass, p)
        self.player.draw()