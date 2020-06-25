# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:28:38 2020

@author: Dana

P2.5.8

"""

#num = list(range(2,10001))
#n = 2
#while n < 10000:
#    for i in num:
#        if((i % n == 0) and (i/n != 1)):
#            num.remove(i)
#    n += 1
#print('Here is a list of all the prime numbers under 10,000:\n\n',num)

#p = 2
#sieve == True
#primes = list(range(2,100))
#marks = [' ']*98
#while sieve == True:
#    for i in primes:
#        if i % p == 0:
#            marks[primes.index(i)] = 'c'
#    p = primes(marks.index[' '])
#print(marks) 
#
#p = 2
##sieve == True
#primes = list(range(2,100))
##while sieve == True:
#for i in primes:
#    if i == 'c':
#        pass
#    elif i % p == 0:
#        i == 'c'
#print(primes) 


#def eratosthenes(n):
#    composites = []
#    for i in range(2, n+1):
#        if i not in composites:
#            for j in range(i*i, n+1, i):
#                composites.append(j)
#    return composites
#
#print(eratosthenes(1000))

#def sieve(n):
#    not_prime = []
#    prime = []
#    xrange = range(2, n+1)
#    for i in xrange:
#        if i not in not_prime:
#            prime.append(i)
#            for j in xrange(i*i, n+1, i):
#                not_prime.append(j)
#    return prime
#sieve(100)

def sieve(n):
    numbers = list(range(2,n+1))
    primes = {}
    p = 2
    for i in numbers:
        primes[i] = True
#    while p < n:
    for j in numbers:
        if j % p == 0:
            primes[j] = False
    for k in numbers:
        if primes[numbers.index(k)] == True:
            p = k
#    print(p)
    return primes
print(sieve(100))





