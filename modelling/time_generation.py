# Расчет скорости генерации вакансии
import numpy as np
from modelling.const_variable import *
import math
import random
from numpy import unravel_index

class TimeGeneration():
    def __init__(self, massiv_potential, massiv_temp):
        self.massiv_time_generation = np.zeros( (SIZE_X, SIZE_Y, SIZE_Z) )
        self.massiv_potential = massiv_potential
        self.massiv_temp = massiv_temp

    def calc(self):
        for self.i in range(0, SIZE_X-1):
            for self.j in range(0, SIZE_Y-1):
                for self.k in range(0, SIZE_Z-1):
                    self.massiv_time_generation[self.i, self.j, self.k] = (
                        -1/(EFECTIVE_FREQ_VIBRATION * math.exp(
                            -(
                                (ENERGY_FORMATION_O_VAC-COEF_COMMUNICATION_POLAR*abs(
                                    0.01*self.massiv_potential[self.i, self.j, self.k])
                                ) * CHARGE_E
                            )/(
                                CONST_BOLTZMAN*self.massiv_temp[self.i, self.j, self.k]
                            )
                        )

                    )
                    ) * math.log(random.random())

    def get_min_value(self):
        self.nmin = np.where(self.massiv_time_generation == np.amin(self.massiv_time_generation))
        print(np.amin(self.massiv_time_generation))
        self.listOfCoordinates = list(zip(self.nmin[0], self.nmin[1], self.nmin[2]))
        return self.listOfCoordinates