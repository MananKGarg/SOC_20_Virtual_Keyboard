# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:20:53 2020

@author: Aanal Sonara
"""


n=int(input())
dict1={}
sub_dict1={}
import numpy as np
for i in range(n):
    data=input()
    data=data.split(":")
    data[1]=data[1].split(',')
    for j in range(len(data[1])):
        data[1][j]=data[1][j].split('-')
        sub_dict1[data[1][j][0]]=int(data[1][j][1])
        dict1[data[0]]=(sub_dict1)
    sub_dict1={}
print(dict1)

final_dict={}
for key, value in dict1.items():
    for player in value:
        if player in final_dict:
            final_dict[player] += value[player]
        else:
            final_dict[player] = value[player]
data =[('name', 'U10'),('score', int)]
final_list = np.array(list(final_dict.items()), dtype=data)
final_list[::-1].sort(order= ['score', 'name'])

print(final_list)
