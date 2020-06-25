# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:33:14 2020

@author: Dana

P2.4.6

"""
import math

# multiply all odds together
x = 7
evens = 1
for i in range(1,x+1):
    if i % 2 == 0:
        evens *= i
print(math.factorial(x)//evens)

# multiply all evens together
y = 10
odds = 1
for j in range(1,y+1):
    if j % 2 == 1:
        odds *= j
print(math.factorial(y)//odds)
        