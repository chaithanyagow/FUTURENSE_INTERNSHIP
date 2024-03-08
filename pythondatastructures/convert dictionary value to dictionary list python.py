# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:03:38 2024

@author: chait
"""


dic_t = {1:'orange',2:'banana',3:'apple',4:'mangoes'}
dict_list = []

for value in dic_t.values():
    dict_item = {"flavours":value}
    dict_list.append(dict_item)
    
print("Dict value to dict list :", dict_list)