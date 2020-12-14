# Рисование кислородных вакансий по существующим координатам.
import numpy as np
import matplotlib.pyplot as plt

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
            self.x_coordinates.append(self.coord[0])
        for self.coord in self.list_coordinates:
            self.y_coordinates.append(self.coord[1])
        self.ax.scatter(self.x_coordinates, self.y_coordinates)
        plt.show()