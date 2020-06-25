# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:31:52 2020

@author: Dana
"""

'''
Part A
1. See the cool graph!
2. There is quite a lot of overlap in the graph. Some notable data points
   are that 1995 held the highest temperature, 2015 held the coldest
   temperature, and 2015 had the warmest December. It is difficult to
   notice any other significant differences with the naked eye.
3. The p-value is 0.271, which is larger than 0.05, so the null hypothesis
   that states that the data are closely related is not rejected. Therefore,
   there is no significant change between the temperatures during the two years.
    
Part B
1. The p-value is less than 0.05 in 144 cities.
2. The average of the difference in average temperatures in 1995 and 2015 of 
   cities with p-value less than 0.05 is 3.771 degrees Fahrenheit.
   
I would expect to find fewer p-values less than 0.05. Definitely fewer than
the 144 that were found, which is a little less than half the files. If all 
the comparisons are from the same distribution, there will be a greater 
chance that they will appear to be from the same distribution, and therefore
the p-value will be higher, closer to 1 than 0.05. The fact that 144 files 
were found that had a really small p-value, indicating that the data are not 
from the same distribution, shows that the likelihood of a real temperature
shift in the past 20 years is great.
'''

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import glob

f = open("MDBALTIM.txt",'rt')
daycount = []
temp = []
years = []
templist = []

for count,line in enumerate(f):
    s = line.split()
    if float(s[-1]) == -99.0:
        continue
    daycount.append(float(count))
    temp.append(float(s[-1]))
    years.append(s[2])
    
yearlist = list(set(years))

for i in yearlist:
    tempbyyear = []
    for j,(a,b) in enumerate(zip(years,temp)):
        if a == i:
            tempbyyear.append(b)
    templist.append(tempbyyear)
dictionary = dict(zip(yearlist,templist))
print(dictionary)
f.close()

fig1 = plt.figure(dpi=100)
plt.plot(daycount,temp)
plt.xlabel('Date (since 1/1/95)')
plt.ylabel('Temperature (F)')

fig2 = plt.figure(dpi=100)
plt.plot(range(0,365),dictionary['1995'],alpha=0.4,lw=2,label='1995')
plt.plot(range(0,365),dictionary['2005'],alpha=0.4,lw=2,label='2005')
plt.plot(range(0,365),dictionary['2015'],alpha=0.4,lw=2,label='2015')
plt.xlabel('Day of the Year')
plt.ylabel('Temperature (F)')
plt.legend()


stat, p = stats.ks_2samp(dictionary['1995'],dictionary['2015'])
print('The p-value of the 2-sample Kolmogorov-Smirnov test for the data from 1995 and 2015 is {:.3f} degrees Fahrenheit.'.format(p))




# Part B Starts

fig3 = plt.figure(dpi=100)

count = 0
p_list = []
avgtempdifferencelowp = []

for file in glob.glob(r'weather/*.txt'):
    f = open(file,'rt')
    
# capture the data for this file similar to Part A
    temp = []
    date = []
    for i,line in enumerate(f):
        s = line.split()
        if len(s)==0: 
            continue # some files have empty lines: ignore them
        date.append(float(i))
        if float(s[-1]) == -99.0:
            if i==0: 
                temp.append(0)
            else: 
                temp.append(temp[-1]) # now we 'smooth over' missing entries
        else:
            temp.append(float(s[-1]))
    templist = []
    
    for i in yearlist:
        tempbyyear = []
        for j,(a,b) in enumerate(zip(years,temp)):
            if a == i:
                tempbyyear.append(b)
        templist.append(tempbyyear)
    
    dictionary = dict(zip(yearlist,templist))
    if len(dictionary['2015']) > 350 and len(dictionary['1995']) > 350:
        stat, p = stats.ks_2samp(dictionary['1995'],dictionary['2015'])
#        print('{} p-value = {:.3f}'.format(file,p))
        p_list.append(p)
        
        # Take the average of 1995 and 2015 temps if p-value is small enough; find difference
        if p < 0.05:
            tempavg1995 = sum(dictionary['1995'])/len(dictionary['1995'])
            tempavg2015 = sum(dictionary['2015'])/len(dictionary['2015'])
            avgtempdifferencelowp.append(tempavg2015-tempavg1995)
        
    f.close()

    plt.plot(date,temp,'m-',lw=0.1,alpha=0.01)
    
# count number of cities with small p-value
for pval in p_list:
    if pval < 0.05:
        count += 1

print("The p-value is less than 0.05 in {} cities.".format(count))
print("The average of the difference in average temperatures in 1995 and 2015 of cities with " + 
      "p-value less than 0.05 is {:.3f}.".format(sum(avgtempdifferencelowp)/len(avgtempdifferencelowp)))

plt.xlabel('Date (since 1/1/95)')
plt.ylabel('Temperature (F)')
plt.show()

