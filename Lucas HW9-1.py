# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:25:39 2020

@author: Dana
"""
import numpy as np
import matplotlib.pyplot as plt
import math

array = np.empty([1000,1000],complex)
array2 = np.empty([1000,1000])
x = np.linspace(-2,2,1000)
y = np.linspace(-2,2,1000)

for a, k in enumerate(x):
    for b, m in enumerate(y):
        array[a][b] = complex(k,m)

for q, n in enumerate(array):
    for r, p in enumerate(n):
        count = 0
        z = complex(0,0)
        while math.hypot(z.real,z.imag)<2 and count<100:
            z = (z**2)+p
            count += 1
        array2[q][r] = count
print(array2)

plt.imshow(array2,cmap='PRGn')