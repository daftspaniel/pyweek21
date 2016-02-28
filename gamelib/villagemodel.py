class VillageModel(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.w = 24
        self.h = 12
        self.map = [[0 for i in range(self.h)] for j in range(self.w)]

        for i in range(self.h):
            self.map[18][i] = 1
            self.map[19][i] = 1
            self.map[23][i] = 2
            self.map[24][i] = 2

