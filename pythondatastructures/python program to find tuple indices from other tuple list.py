# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:02:16 2024

@author: chait
"""

def find_indices(main_tuple, search_tuple):
    return [main_tuple.index(element) if element in main_tuple else None for element in search_tuple]

main_tuple = tuple(input("Enter the elements of main tuple ").split(','))
search_tuple = tuple(input("Enter the elements u want indices of  ").split(','))


result_indices = find_indices(main_tuple, search_tuple)

print(f"Indices of elements from search_tuple in main_tuple: {result_indices}")