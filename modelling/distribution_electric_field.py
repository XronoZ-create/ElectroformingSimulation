# Первый этап моделирования. Рассчет расперделения электрического поля в обьеме оксидной пленки
import numpy as np
from modelling.const_variable import *

class DistributionElectricField():
    def __init__(self):
        self.massiv_potential = np.zeros( (SIZE_X, SIZE_Y, SIZE_Z) )
        self.massive_for_check_vacancies = np.zeros( (SIZE_X, SIZE_Y, SIZE_Z) )
    def calc(self):
        for self.iter_cycleElect in range(1, 300):
            for self.i in range(0, SIZE_X-1):
                for self.j in range(0, SIZE_Y-1):
                    self.massiv_potential[self.i, self.j, 0] = POTENTIAL_O_VAC
                    self.massiv_potential[self.i, self.j, SIZE_Z-1] = 0

            for self.k in range(1, SIZE_Z-2):
                for self.i in range(0, SIZE_X-1):
                    for self.j in range(0, SIZE_Y-1):
                        if self.i == 0:
                            self.massiv_potential[0, self.j, self.k] = self.massiv_potential[1, self.j, self.k]
                            continue

                        if self.i == SIZE_X-1:
                            self.massiv_potential[SIZE_X-1, self.j, self.k] = self.massiv_potential[SIZE_X-2, self.j, self.k]
                            continue

                        self.massiv_potential[self.i, 0, self.k] = self.massiv_potential[self.i, 1, self.k]
                        self.massiv_potential[self.i, SIZE_Y-1, self.k] = self.massiv_potential[self.i, SIZE_Y-2, self.k]

            for self.i in range(1, SIZE_X-2):
                for self.j in range(1, SIZE_Y-2):
                    for self.k in range(1, SIZE_Z-2):
                        self.q = 0
                        if self.massive_for_check_vacancies[self.i, self.j, self.k] == 1:
                            self.q = POTENTIAL_O_VAC
                        self.massiv_potential[self.i, self.j, self.k] = (
                            self.massiv_potential[self.i+1, self.j, self.k] +
                            self.massiv_potential[self.i-1, self.j, self.k] +
                            self.massiv_potential[self.i, self.j+1, self.k] +
                            self.massiv_potential[self.i, self.j-1, self.k] +
                            self.massiv_potential[self.i, self.j, self.k+1] +
                            self.massiv_potential[self.i, self.j, self.k-1] +
                            (self.q/DIELECTRIC_CONST)
                        )/6

            for self.i in range(0, SIZE_X-1):
                for self.j in range(0, SIZE_Y-1):
                    self.massiv_potential[self.i, self.j, 0] = POTENTIAL_O_VAC
                    self.massiv_potential[self.i, self.j, SIZE_Z-1] = 0

            for self.k in range(1, SIZE_Z-2):
                for self.i in range(0, SIZE_X-1):
                    for self.j in range(0, SIZE_Y-1):
                        if self.i == 0:
                            self.massiv_potential[0, self.j, self.k] = self.massiv_potential[1, self.j, self.k]
                            continue
                        if self.i == SIZE_X-1:
                            self.massiv_potential[SIZE_X-1, self.j, self.k] = self.massiv_potential[SIZE_X-2, self.j, self.k]
                            continue
                        self.massiv_potential[self.i, 0, self.k] = self.massiv_potential[self.i, 1, self.k]
                        self.massiv_potential[self.i, SIZE_Y-1, self.k] = self.massiv_potential[self.i, SIZE_Y-2, self.k]

            for self.j in range(SIZE_Y-2, 1, -1):
                for self.i in range(SIZE_X-2, 1, -1):
                    for self.k in range(SIZE_Z-2, 1, -1):
                        self.q = 0
                        if self.massive_for_check_vacancies[self.i, self.j, self.k] == 1:
                            self.massiv_potential[self.i, self.j, self.k] = POTENTIAL_O_VAC
                        else:
                            self.massiv_potential[self.i, self.j, self.k] = (
                                self.massiv_potential[self.i+1, self.j, self.k] +
                                self.massiv_potential[self.i-1, self.j, self.k] +
                                self.massiv_potential[self.i, self.j+1, self.k] +
                                self.massiv_potential[self.i, self.j-1, self.k] +
                                self.massiv_potential[self.i, self.j, self.k+1] +
                                self.massiv_potential[self.i, self.j, self.k-1] +
                                (self.q/DIELECTRIC_CONST)
                            )/6