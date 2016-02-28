from gamelib.util import *
#from gamelib.symbols import *

import os


class GFXStore(object):
    def __init__(self):
        # Characters
        self.amy = self.LoadGFX("img/amy.png", True)

        # Scene
        self.grass = self.LoadGFX("img/grass.png", False)

    def LoadGFX(self, path, transparentbg):
        if path.find(os.sep) == -1:
            filename = path.replace("/", os.sep)

        i = pygame.image.load(path).convert()
        if transparentbg:
            i.set_colorkey((0, 0, 0))
        return i