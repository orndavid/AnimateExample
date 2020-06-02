"""
Animating a search for equilibrium inside a container here the objective
of each particle is to push away from the closest one
"""

import numpy as np

import matplotlib.pyplot as plt
import  matplotlib.animation as animation
from scipy.spatial.distance import cdist


class Particles:
    def __init__(self, n, width=4, pressure=0.045, mindist=None):
        """ Width is the width of the window, creating the boundaries"""
        self.n = n
        self.P = np.random.uniform(high = width, size=(n, 2))
        self.pressure = pressure
        if mindist:
            self.mindist = mindist
        else:
            area = 4.0**2.0
            self.mindist = area/n*1.825
            print(self.mindist)
        self.step_count = 0
        self.minv = None

    def step(self):
        """Update location of points"""
        # Compute the distance
        dist = cdist(self.P, self.P, "euclidean")
        self.minv = np.sort(dist, axis=1)[:, 1]
        # Stop if distance is more than mindist
        self.minv[self.minv > self.mindist] = 0.0

        temp = self.P
        for indx, point in enumerate(self.P):
            push_point = np.where(dist[indx, :] == self.minv[indx])[0][0]
            direction = (point-self.P[push_point, :])
            temp[indx] = self.conserve_bounds(point + self.pressure*direction)

        self.P = temp
        self.step_count += 1

    def conserve_bounds(self, point):
        #TODO refactor for a more generic approach
        point[point < 0.0] = 0.0
        point[point > 4.0] = 4.0
        return point

    def points(self):
        return self.P
    
def test():
    plt.close("all")
    global obj, figure, points, ax
    figure = plt.figure()
    ax = figure.add_subplot(111, autoscale_on=False, aspect="equal", xlim=(-1, 5), ylim=(-1, 5))
    ax.grid("on")
    obj = Particles(400)
    points_c, = ax.plot([], [], 'bo', ms=2)
    points_f, = ax.plot([], [], 'ro', ms=2)
    
   
    def ani_func_call(i):
        global figure, obj, points, ax
        obj.step()

        red_block = abs(obj.minv) < 1e-6
        red = obj.P[red_block, :]
        blue = obj.P[~red_block, :]
        points_f.set_data(red[:, 0], red[:, 1])
        points_c.set_data(blue[:, 0], blue[:, 1])

        return points_c, points_f, 
       
    axni = animation.FuncAnimation(figure, ani_func_call, frames=500,
                                  interval=75, blit=True)
    # count = 0
    # while(True):
    #     ani_func_call(count)
    #     count += 1
    plt.show()
    print("Finished")
                                  

test()
