# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:24:29 2020

@author: Dana

Q2.5.2

"""
import math as m
x = [1]
y = [m.sqrt(2)]
while x[-1] != y[-1]:
        x.append(0.5*(x[-1]+y[-1]))
        y.append(m.sqrt(x[-2]*y[-1])) 
        #   use x[-2] because if not, the calculation will use 
        #   the value of x that was just added in the previous line
        print(x[-1],y[-1])
print("Gauss's constant is: ", 1/x[-1])