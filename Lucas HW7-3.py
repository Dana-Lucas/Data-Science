# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:33:01 2020

@author: Dana
P2.7.5 Refer back to P2.7.5. Plot (on the same panel) R and H for v = 10ms−1 and α varying
smoothly from 0◦ to 90◦.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def projectile(v):
    a = np.linspace(0,90,50)
    R = []
    H = []
    for i in a:
        R.append(((v**2)*math.sin(2*math.radians(i)))/9.81)
        H.append(((v**2)*(math.sin(math.radians(i)))**2)/(2*9.81))
    
    fig = plt.figure(dpi=100)
    plt.plot(a,R,label = 'Range')
    plt.plot(a,H,label = 'Maximum Height')
    plt.xlabel('Angle (degrees)', size = 'large')
    plt.ylabel('Distance (m)', size = 'large')
    plt.title('Projectile Launch', size = 'x-large')
    plt.legend(loc = 'upper left')
    plt.show()
    
projectile(10)