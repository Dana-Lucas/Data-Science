# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:09:30 2020

@author: Dana

Q2.4.7

"""

month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sun = [44.7,65.4,101.7,148.3,170.9,171.4,176.7,186.1,133.9,105.4,59.6,45.8]
z = sorted(list(zip(sun,month)))
z.reverse()
print(z)
