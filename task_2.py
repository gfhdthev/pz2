#Gfhdthev
#Практическое занятие, задание 2

import matplotlib.pyplot as plt
import matplotlib.patches

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

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

first = Circle(0, 0, 5)
first.graf()