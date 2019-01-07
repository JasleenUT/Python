#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 07:02:18 2019

@author: jasleenarora
"""

## Task
# You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N. 
# You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal to N.

'''Sample Input 0
1
1
1
2'''

'''Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )])