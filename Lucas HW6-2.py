# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:44:36 2020

@author: Dana
P2.7.5
"""
import math

def projectile(v,a):
    a = math.radians(a)
    R = ((v**2)*math.sin(2*a))/9.81
    H = ((v**2)*(math.sin(a))**2)/(2*9.81)
    return R,H

print('The range of the projectile is {:.3f} meters and the height is {:.3f} meters.'.format(projectile(10,30)[0],projectile(10,30)[1]))
    