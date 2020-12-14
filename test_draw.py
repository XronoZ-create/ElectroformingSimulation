from draw.draw_vacancies import DrawVacancies
import numpy as np

n = np.zeros((2, 2, 2))
n[0,0,1] = 1

nmax = np.where(n == np.amax(n))
print(np.amax(n))
listOfCoordinates = list(zip(nmax[0], nmax[1], nmax[2]))
print(listOfCoordinates)
d = DrawVacancies()

d.add_vacancies(listOfCoordinates)
d.draw()