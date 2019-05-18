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

class KMeans:
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

    def sample_data(self,samples=50):
        self.x = [[r(), r()] for _ in range(samples)]

    def show(self):


    def assign_kentroidi(self,x):
        distances = {}
        for kentroidi in self.kentroidi:
            distances[kentroidi] = np.linalg.norm(kentroidi.pos - x)
        closest = min(distances.items(), key=operator.itemgetter(1))[0]
        return closest

    def _update_kentroidi(self, reset=True):
        for kentroidi in self.kentroidi:
            kentroidi.previous_points = kentroidi.points
            x_coord = [x[0] for x in kentroidi.points]
            y_coord = [y[1] for y in kentroidi.points]
            try:
                kentroidi.pos[0] = sum(x_coord)/len(x_coord)
                kentroidi.pos[1] = sum(y_coord)/len(y_coord)
            except:
                pass

            if reset:
                kentroidi.points = []
    def fit(self):
        self.n_epanalipseis = 0
        fit = False
        while not fit:
            for point in self.x:
                closest = self.assign_kentroidi(point)
                closest.points.append(point)
            if len([c for c in self.kentroidi if c.points == c.previous_points]) == self.n_kentroidi:
                fit = True
                self._update_kentroidi(reset=False)
            else:
                self._update_kentroidi()
            self.n_epanalipseis += 1





if __name__ == '__main__':
    km = KMeans()
    km.sample_data()
    km.assign_kentroidi(km.x[0])
