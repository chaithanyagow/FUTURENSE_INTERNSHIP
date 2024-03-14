# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:48:13 2024

@author: chait
"""
# write a python program to flatten tuple of list to tuple
#tuple of list
x = ([3, 4, 5], [53,63],[7,8,9])
y=[]
for i in x:
    for number in i:
        y.append(number)
z=tuple(y)
print(z)



