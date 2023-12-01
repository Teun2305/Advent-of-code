# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:48:11 2022

@author: teunh
"""

file = open('input_dec_2.txt', 'r')

moves = list()

for move in file:
    m1, m2 = move.split()
    assert m1[0] != m2[0]
    moves.append((m1, m2.strip()))

# Nicely hardcoded fucntions

def result(their_move, your_move):
    if their_move == 'rock':
        if your_move == 'rock':
            return 3
        elif your_move == 'paper':
            return 6
        elif your_move == 'scissors':
            return 0
        
    elif their_move == 'paper':
        if your_move == 'rock':
            return 0
        elif your_move == 'paper':
            return 3
        elif your_move == 'scissors':
            return 6
        
    elif their_move == 'scissors':
        if your_move == 'rock':
            return 6
        elif your_move == 'paper':
            return 0
        elif your_move == 'scissors':
            return 3
    else: raise ValueError
    
def get_your_move(their_move, result):
    if their_move == 'rock':
        if result == 'won':
            return 'paper'
        elif result == 'drew':
            return 'rock'
        elif result == 'lost':
            return 'scissors'
        
    elif their_move == 'paper':
        if result == 'won':
            return 'scissors'
        elif result == 'drew':
            return 'paper'
        elif result == 'lost':
            return 'rock'
        
    elif their_move == 'scissors':
        if result == 'won':
            return 'rock'
        elif result == 'drew':
            return 'scissors'
        elif result == 'lost':
            return 'paper'
        
    else: raise ValueError
    
scores = {
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3,
    'won' : 6,
    'drew' : 3,
    'lost' : 0
    }

their_move_meaning = {
    'A' : 'rock',
    'B' : 'paper',
    'C' : 'scissors'
    }

your_move_meaning1 = {    
    'X' : 'rock',
    'Y' : 'paper',
    'Z' : 'scissors' 
    }

your_move_meaning2 = {
    'X' : 'lost',
    'Y' : 'drew',
    'Z' : 'won' 
    }

total_score = 0
for m1, m2 in moves:
    their_move = their_move_meaning[m1]
    your_move = your_move_meaning1[m2]
    r = result(their_move, your_move)
    total_score += scores[your_move] + r

print(f'Answer part 1: {total_score}')

total_score = 0
for m1, m2 in moves:
    their_move = their_move_meaning[m1]
    r = your_move_meaning2[m2]
    your_move = get_your_move(their_move, r)
    total_score += scores[your_move] + scores[r]
    
print(f'Answer part 2: {total_score}')
    

    
