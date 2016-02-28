from gamelib.util import *
# from gamelib.symbols import *

import os


class GFXStore(object):
    def __init__(self):

        load = self.LoadGFX
        # Characters
        self.amy = load("img/amy.png", True)
        self.bill = load("img/bill.png", True)
        self.cam = load("img/cam.png", True)

        # Buildings
        self.tent = load("img/tent.png", True)
        self.campfire = load("img/campfire.png", True)

        # Scene
        self.grass = load("img/grass.png")
        self.sand = load("img/sand.png")
        self.water = [load("img/water1.png"), load("img/water2.png"), load("img/water3.png")]

        self.images = {}
        self.images[0] = self.grass
        self.images[1] = self.water[0]
        self.images[2] = self.sand
        self.images[100] = self.tent
        self.images[101] = self.campfire

    def LoadGFX(self, path, transparentbg=False):
        if path.find(os.sep) == -1:
            filename = path.replace("/", os.sep)

        i = pygame.image.load(path).convert()
        if transparentbg:
            i.set_colorkey((0, 0, 0))
        return i

    def getWater(self):
        return self.water[RND(3) - 1]

    def getById(self, id):
        return self.images[id]
