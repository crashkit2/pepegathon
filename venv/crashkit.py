import numpy as np
import operator
import matplotlib.pyplot as plt
import matplotlib.cm as cm

r = lambda: np.random.randint(1,100)

class Kentroidi:
    def __init__ (self,pos):
        self.pos = pos
        self.points = []
        self.previouspoints = []
        self.color = None

class Kmeans:
    def __init__(self, n_kentroidi=5):
        self.n_kentroidi = n_kentroidi
        self.kentroidi = []

        # dimiourgia arxikwn kentroidwn
        for _ in range(n_kentroidi):
            self.kentroidi.append(Kentroidi(np.array([r(),r()])))

        # anathetisi xrwmatos gia to kathe kentroides
        colors = cm.rainbow(np.linspace(0,1, len(self.kentroidi)))
        for i, c in enumerate(self.kentroidi):
            c.color = colors[i]

