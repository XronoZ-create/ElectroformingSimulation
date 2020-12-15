# Рисование кислородных вакансий по существующим координатам.
import numpy as np
import matplotlib.pyplot as plt
from modelling.const_variable import *
import matplotlib.ticker as ticker

class DrawVacancies():
    def __init__(self):
        self.list_coordinates = []

    def add_vacancies(self, coordinate):
        self.list_coordinates.append(coordinate[0])

    def draw(self):
        self.fig, self.ax = plt.subplots()
        self.x_coordinates = []
        self.y_coordinates = []
        for self.coord in self.list_coordinates:
            self.x_coordinates.append(self.coord[0]-0.5)
        for self.coord in self.list_coordinates:
            self.y_coordinates.append(self.coord[1]-0.5)
        self.ax.scatter(self.x_coordinates, self.y_coordinates, s=1000)

        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.set_xlim(0, SIZE_X)
        self.ax.set_ylim(0, SIZE_Y)
        plt.grid(True)
        plt.show()