# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:06:58 2020

@author: Dana

P2.4.1

"""

a = [1,2,3,4,5,6]
total = 1
print(type(total))
for i in a:
    total *= i
z = []
for j in a:
    z.append(total//j)
print(z)