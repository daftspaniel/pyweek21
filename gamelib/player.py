import pygame
from pygame.locals import *


class Player(object):
    def __init__(self, image, surface, pos=(0, 0)):

        self.surface = surface
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.vmove = 0
        self.hmove = 0

    def update(self):

        if self.hmove != 0:
            self.rect.left += self.hmove
        if self.vmove != 0:
            self.rect.top += self.vmove

        if self.rect.left > 708:
            self.rect.left = 708
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top > 584:
            self.rect.top = 584
        if self.rect.top < 32:
            self.rect.top = 32

    def draw(self):
        self.update()
        self.surface.blit(self.image, self.rect)
