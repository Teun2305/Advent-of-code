# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:16:53 2022

@author: teunh
"""

with open('input_dec_4.txt', 'r') as file:
    counter1 = 0
    counter2 = 0
    for line in file:
        r1, r2 = line.split(',')
        start1, stop1 = r1.split('-')
        start2, stop2 = r2.split('-')
        
        start1, stop1, start2, stop2 = int(start1), int(stop1), int(start2), int(stop2)
        set1 = set([x for x in range(start1, stop1 + 1)])       
        set2 = set([x for x in range(start2, stop2 + 1)])
        
        if set1.issubset(set2) or set2.issubset(set1):
            counter1 += 1
            
        if len(set1.intersection(set2)) > 0:
            counter2 += 1
            
print(f'Answer part 1: {counter1}')
print(f'Answer part 2: {counter2}')