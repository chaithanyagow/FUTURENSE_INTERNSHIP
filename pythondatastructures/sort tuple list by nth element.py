# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:53:41 2024

@author: chait
"""

grocery__list = [(1, 'virat'), (2, 'rohit'), (3, 'bumrah'), (4, 'jadeja')]
n = 1 
grocery__list.sort(key=lambda x: x[n])
print(grocery__list)
