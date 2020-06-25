# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:24:46 2020

@author: Dana
Q8.2.2 b and c
"""
from scipy import integrate
import numpy as np

def f(x): return x**3/(np.exp(x)-1)

val1,error=integrate.quad(f,0,np.inf)
val1_actual = ((np.pi)**4)/15
 
print("Quad gives: \t\t{}".format(val1))
print("Compare this to: \t{}".format(val1_actual))
print()
#-------------------------------------------------------------
def g(x): return x**(-x)

val2,error=integrate.quad(g,0,1)
val2_actual = 0
val2_list = [i**(-i) for i in range(1,1000000)]
for i in val2_list:
    val2_actual += i

print("Quad gives: \t\t{}".format(val2))
print("Compare this to: \t{}".format(val2_actual))
