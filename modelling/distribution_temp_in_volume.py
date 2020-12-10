#Расчет распределения температуры в обьеме оксидной пленки
import numpy as np
from modelling.const_variable import *

class DistributionTempInVolume():
    def __init__(self):
        self.massiv_temp = np.zeros( (SIZE_X, SIZE_Y, SIZE_Z) )
        self.massive_for_check_vacancies = np.zeros((SIZE_X, SIZE_Y, SIZE_Z))
        self.massive_help_for_temp = np.zeros((SIZE_X, SIZE_Y, SIZE_Z))

    def calc(self):
        for self.iter_cycleTemp in range(0, 100-1):
            for self.i in range(0, SIZE_X-1):
                for self.j in range(0, SIZE_Y-1):
                    for self.k in range(0, SIZE_Z-1):
                        if self.i == SIZE_X-1:
                            self.t1 = 300
                        else:
                            self.t1 = self.massiv_temp[self.i+1, self.j, self.k]

                        if self.i == 0:
                            self.t2 = 300
                        else:
                            self.t2 = self.massiv_temp[self.i-1, self.j, self.k]

                        if self.j == SIZE_Y-1:
                            self.t3 = 300
                        else:
                            self.t3 = self.massiv_temp[self.i, self.j+1, self.k]

                        if self.j == 0:
                            self.t4 = 300
                        else:
                            self.t4 = self.massiv_temp[self.i, self.j-1, self.k]

                        if self.k == SIZE_Z-1:
                            self.t5 = 300
                        else:
                            self.t5 = self.massiv_temp[self.i, self.j, self.k+1]

                        if self.k == 0:
                            self.t6 = 300
                        else:
                            self.t6 = self.massiv_temp[self.i, self.j, self.k-1]

                        self.q = 0
                        if self.massive_for_check_vacancies[self.i, self.j, self.k] == 1:
                            self.q = TEMP_O_VAC

                        self.massive_help_for_temp[self.i, self.j, self.k] = (
                                self.massiv_temp[self.i, self.j, self.k] +
                                0.08*(self.t1-2 *self.massiv_temp[self.i, self.j, self.k]+self.t2)*dt/(h*h*h)+
                                0.08*(self.t3-2*self.massiv_temp[self.i, self.j, self.k]+self.t4)*dt/(h*h*h)+
                                4*(self.t5-2*self.massiv_temp[self.i, self.j, self.k]+self.t6)*dt/(h*h*h)+
                                (self.q*dt)
                                )

            for self.i in range(0, SIZE_X - 1):
                for self.j in range(0, SIZE_Y - 1):
                    for self.k in range(0, SIZE_Z - 1):
                        self.massiv_temp[self.i, self.j, self.k] = self.massive_help_for_temp[self.i, self.j, self.k]
