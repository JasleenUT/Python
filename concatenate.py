#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:32:50 2019

@author: jasleenarora
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:32:10 2019

@author: jasleenarora
"""
##Task
#You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). 
#Your task is to concatenate the arrays along axis.

##Input Format
#The first line contains space separated integers N,M and P. 
#The next N lines contains the space separated elements of the P columns. 
#After that, the next M lines contains the space separated elements of the P columns.


##Output Format
#Print the concatenated array of size (N+M)XP.

'''Sample Input
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 '''


'''Sample Output
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] '''


import numpy
nmp = input()
nmp = nmp.split()
nmp = list(map(int,nmp))
n = nmp[0]
m = nmp[1]
p = nmp[2]


np = []
for i in range(0,n):
    temp = input()
    temp = temp.split()
    temp = list(map(int,temp))
    np.append(temp)



mp = []
for i in range(0,m):
    temp = input()
    temp = temp.split()
    temp = list(map(int,temp))
    mp.append(temp)

print(numpy.concatenate((np,mp),axis=0))