# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:19:17 2020

@author: Dana

P2.4.7 part 1

"""

n = 500
sum = 0
fib = [1,1]
list = [0.301,0.176,0.125,0.097,0.079,0.067,0.058,0.051,0.046]
for n in range(n-2):
    fib.append(fib[-1]+fib[-2])
for j in range(1,10):
    for i in fib:
        x=str(i)
        if x[0] == str(j):
            sum += 1
    prob = sum/len(fib)
    error = 100*(prob-list[j-1])/list[j-1]
    print(j,': {:.3f}'.format(prob), "\tpercent error:",'{: .2f}%'.format(-error))
    sum = 0
    
# The fibonacci numbers follow Benford's law because each is within 6% of the predicted probability.