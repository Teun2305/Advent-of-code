# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:53:51 2022

@author: teunh
"""
file = open('input_dec_1.txt', 'r')
        
elfs = list()
total_cal = 0
for cal in file:
    if cal == '\n':
        elfs.append(total_cal)
        total_cal = 0
        continue
    total_cal += int(cal)
elfs.append(total_cal)

elfs.sort(reverse=True)
print(f'Answer part 1: {elfs[0]}')
print(f'Answer part 2: {sum(elfs[:3:])}')
