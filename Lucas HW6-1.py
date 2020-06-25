# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:43:03 2020

@author: Dana
Q2.7.3
"""

def digit_sum(n):
    """ Find the sum of the digits of integer n. """
    
    s_digits = list(str(n))
    dsum = 0
    for s_digit in s_digits:
        dsum += int(s_digit)
    return dsum # This definition doesn't return anything (becomes none) unless told to do so. Adding this line fixes the issue
        
def is_harshad(n):
    return not n % digit_sum(n)

print(is_harshad(21))
print(is_harshad(14))
print(is_harshad(54))