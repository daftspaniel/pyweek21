import random
import pygame
from pygame.locals import *


def draw_village(model, surface, gfx):
    for x in range(0, model.w):
        for y in range(0, model.h):
            p = Rect(x * 32, y * 32, 32, 32)

            surface.blit(gfx.getById(model.map[x][y]), p)
            # if x == 10:
            #     surface.blit(gfx.getWater(), p)
            # else:
            #     surface.blit(gfx.grass, p)
            #
            # if x == 20 and y==10:
            #     surface.blit(gfx.tent, p)
