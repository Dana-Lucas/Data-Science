# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:32:47 2020

@author: Dana
P3.3.1
"""
import matplotlib.pyplot as plt
import numpy as np
import math

r1 = []
r2 = []

a = 0
b = 2
fig = plt.figure(dpi = 150)
theta = np.linspace(0,math.pi*8,500)
for i in theta:
    r1.append(a+b*i)
    r2.append(0.8**i)
ax1 = plt.subplot(121, projection = 'polar')
plt.polar(theta,r1)
plt.title('Archimedean Spiral')
ax2 = plt.subplot(122, projection = 'polar')
plt.polar(theta,r2)
plt.title('Logarithmic Spiral')
plt.show()