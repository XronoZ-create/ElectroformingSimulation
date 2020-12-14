import numpy as np
from modelling.const_variable import *

a = np.zeros( (SIZE_X, SIZE_Y, SIZE_Z) )

for i in range(0, SIZE_X):
    for j in range(0, SIZE_Y):
        for k in range(0, SIZE_Z):
            if i == 0 and j == 0 and k == 18:
                a[i, j, k] = 1

print(a[0, 0, 18])