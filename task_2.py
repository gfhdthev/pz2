#Gfhdthev
#Практическое занятие, задание 2

import matplotlib as mtl
import matplotlib.pyplot as plt
import matplotlib.patches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Circle:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.r = r
        self.z = z

    def graf(self):

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        plt.grid()
        axes = plt.gca()
        
        circle_r = matplotlib.patches.Circle((self.x, self.y), radius=self.r, fill = False, color = 'black')
        axes.add_patch(circle_r)

        plt.show()

    def __del__(self):
        print('Окружность удалена')



class Ball(Circle):
    def __init__(self, x, y, z, r):
        super().__init__(x, y, r)
        self.z = z

    def graf(self):
        self.fig = plt.figure(figsize=(10,10))
        self.ax = self.fig.add_subplot(111, projection = '3d')

        self.u = np.linspace(0, 2 * np.pi, 100)
        self.v = np.linspace(0, np.pi, 100)

        self.x = self.r * np.outer(np.cos(self.u), np.sin(self.v)) + self.x
        self.y = self.r * np.outer(np.sin(self.u), np.sin(self.v)) + self.y
        self.z = self.r * np.outer(np.ones(np.size(self.u)), np.cos(self.v)) + self.z

        self.ax.plot_surface(self.x, self.y, self.z, color='b')

        plt.show()

    def __del__(self):
        print(f'Шар удален')

first = Ball(0, 0, 0, 5)
first.graf()