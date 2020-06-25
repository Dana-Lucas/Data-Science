# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:26:22 2020

@author: Dana
P8.2.1
"""
from scipy import integrate
import numpy as np

def f(x):
    return 2*np.pi*np.sqrt(x)*np.sqrt(1+(1/(2*np.sqrt(x)))**2)

val,error = integrate.quad(f,0,1)
val_actual = np.pi*(5**(3/2)-1)/6

print("Quad gives: \t{}".format(val))
print("It should be: \t{}".format(val_actual))

