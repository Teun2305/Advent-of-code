# import numpy as np
import string
from queue import Queue

with open('input_dec_12.txt', 'r') as file:
    f = file.readlines()

heights = dict()
for row, letter in enumerate(string.ascii_lowercase):
    heights[letter] = row
heights['S'] = 0
heights['E'] = 25


class Square:
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.height = heights[symbol]
        self.row, self.col = row, col
        self.parent = None

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return self.col == other.col and self.row == other.row

    def __str__(self):
        return self.symbol


grid = list()
for row, line in enumerate(f):
    this_row = list()
    line = line.strip('\n')
    for col, square in enumerate(line):
        s = Square(square, row, col)
        if square == 'S':
            S = s
        elif square == 'E':
            E = s
        this_row.append(s)
    grid.append(this_row)


def get_neighbours(s):
    neighbours = list()
    if s.col + 1 < len(grid[0]) and grid[s.row][s.col+1].height - s.height <= 1:
        neighbours.append(grid[s.row][s.col+1])
    if s.col - 1 >= 0 and grid[s.row][s.col-1].height - s.height <= 1:
        neighbours.append(grid[s.row][s.col-1])
    if s.row + 1 < len(grid) and grid[s.row+1][s.col].height - s.height <= 1:
        neighbours.append(grid[s.row+1][s.col])
    if s.row - 1 >= 0 and grid[s.row-1][s.col].height - s.height <= 1:
        neighbours.append(grid[s.row-1][s.col])
    
    return neighbours


def reset_parents():
    for row in grid:
        for s in row:
            s.parent = None


def bfs(root, goal, part2):
    explored = list()
    explored.append(root)
    q = Queue()
    q.put(root)

    while not q.empty():
        v = q.get()
        if v is goal:
            return v

        for w in get_neighbours(v):
            if w not in explored:
                explored.append(w)
                w.parent = v
                q.put(w)


def get_path(v, path, part2):
    path.append(v)
    if v.parent is None or v.symbol == 'a' and part2:
        return path
    else:
        return get_path(v.parent, path, part2)


bfs(S, E, False)
print(f'Answer part 1: {len(get_path(E, list(), False))-1}')
reset_parents()
bfs(grid[27][0], E, True)
print(f'Answer part 2: {len(get_path(E, list(), True))-1}')
    