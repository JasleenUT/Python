#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:47:26 2019

@author: jasleenarora
"""

#You are given a space separated list of nine integers. 
#Your task is to convert this list into a 3X3 NumPy array.

#Input Format
#A single line of input containing  space separated integers.

#Output Format
#Print the 3X3 NumPy array.

#Sample Input
#1 2 3 4 5 6 7 8 9

#Sample Output
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

import numpy
arr = input()
arr = arr.split()
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
arr1 = numpy.array(arr)
arr1.shape = (3,3)
print(arr1)
