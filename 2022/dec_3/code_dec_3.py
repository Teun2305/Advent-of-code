# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:30:27 2022

@author: teunh
"""

import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

letters = '0' + string.ascii_lowercase + string.ascii_uppercase

with open('input_dec_3.txt', 'r') as file:
    rucksacks = [x.strip('\n') for x in file]
    
total_score = 0
for r in rucksacks:
    s1 = set(r[:len(r)//2:])
    s2 = set(r[len(r)//2::])
    duplicates = s1.intersection(s2)
            
    for d in duplicates:
        total_score += letters.index(d)
    
print(f'Answer part 1: {total_score}')

total_score = 0
for i in range(0, len(rucksacks), 3):
    s1 = set(rucksacks[i])
    s2 = set(rucksacks[i+1])
    s3 = set(rucksacks[i+2])
    
    badges = s1.intersection(s2).intersection(s3)
    
    for b in badges:
        total_score += letters.index(b)
        
print(f'Answer part 2: {total_score}')
    