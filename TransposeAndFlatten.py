#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:47:26 2019

@author: jasleenarora
"""

#Task
#You are given a NXM integer array matrix with space separated elements (N = rows and M = columns). 
#Your task is to print the transpose and flatten results.

#Input Format
#The first line contains the space separated values of N and M . 
#The next N lines contains the space separated elements of M columns.

#Output Format
#First, print the transpose array and then print the flatten.

'''Sample Input

2 2
1 2
3 4'''


'''Sample Output
[[1 3]
 [2 4]]
[1 2 3 4]'''

import numpy

# Input the size of the matrix
nm = input("Enter the size of the matrix")
nm = nm.split()
# Convert it into integer
nm = list(map(int,nm))

# Input the matrix
arr = []
for i in range(0,nm[0]):
    a = input("Enter the values")
    arr.append(a)

for i in range(0,len(arr)):
    arr[i] = arr[i].split()
    arr[i] = list(map(int,arr[i]))

arr = numpy.array(arr)

# Transpose array
print(numpy.transpose(arr))

# Flatten the array
print(arr.flatten())