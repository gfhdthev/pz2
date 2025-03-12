#Gfhdthev
#Практическое занятие


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

class Parabola:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def korni(self):
        self.disc = self.b**2 - 4*self.a*self.c

        if self.disc < 0:
            print('Уравление не имеет корней')

        elif self.disc == 0:
            self.one_x = (-self.b)/self.a*2
            print(f'Уравнение имеет один корень {self.one_x}')

        else:
            self.x1 = (-self.b + sqrt(self.disc))/self.a*2
            self.x2 = (-self.b - sqrt(self.disc))/self.a*2
            print(f'Первый конень уравнения: {self.x1}')
            print(f'Второй конень уравнения: {self.x2}')

    def graf(self):
        self.x = np.linspace(-10, 10, 50)
        self.y = self.a*self.x**2 + self.b*self.x + self.c  

        fig, self.ax = plt.subplots()

        self.ax.plot(self.x, self.y, color='blue') #создаем пометку 
        self.ax.set_title('График функции y') #подписываем весь график
        self.ax.set_xlabel('Ось x') #подписываем ось x
        self.ax.set_ylabel('Ось y') #подписываем ось y
        self.ax.grid() #устанавливаем сетку, чтобы лучше ориентироваться

        self.ax.set_xlim(-10, 10) #устанавливаем изначальный вид функции
        self.ax.set_ylim(-10, 10) 
        
    def show(self):   
        self.graf()
        plt.show() #выводим график

    def __del__(self):
        print('Парабола отрисована')


class Line(Parabola):

    def __init__(self,a ,b, c, d):
        super().__init__(a, b, c, d)

    def graf(self):
        super().graf()
        self.x = np.linspace(-10, 10, 2)
        self.y = self.a*self.x + self.b

        self.ax.plot(self.x, self.y, color='red') #создаем пометку 


    def __del__(self):
        print('Прямая удалена')

class Kube(Parabola):

    def __init__(self,a ,b, c, d):
        super().__init__(a, b, c, d)

    def graf(self):
        super().graf()
        self.x = np.linspace(-10, 10, 100)
        self.y = self.a*self.x**3 + self.b*self.x**2 + self.c*self.x + self.d

        self.ax.plot(self.x, self.y, color='red') #создаем пометку 


    def __del__(self):
        print('Кубическое уравнение удалено')

first = Kube(10, 70, -32, 0)
first.show()