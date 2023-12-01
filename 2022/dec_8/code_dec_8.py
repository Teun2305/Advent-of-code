import numpy as np

with open('input_dec_8.txt', 'r') as file:
    trees = list()
    for row in file:
        row = row.strip('\n')
        trees.append([int(x) for x in row])

grid = np.array(trees)

counter = 0
visible = 0
max_score = float('-inf')
for i, row in enumerate(grid):
    for j, field in enumerate(row):
        col = grid[:,j]
        left, right = row[:j:], row[j+1::]
        top, bottom = col[:i:], col[i+1::]
        directions = [left, top, right, bottom]

        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(row) - 1:
            visible += 1
        else:
            small_tree = min([max(x) for x in directions])
            if small_tree < field:
                visible += 1
        
        score = 1
        for k, array in enumerate(directions):
            if k < 2 and len(array) > 1:
                array = array[::-1]

            cur_score = 0
            for tree in array:
                cur_score += 1
                if tree >= field:
                    break

            score *= cur_score
        max_score = max(max_score, score)

print(f'Answer part 1: {visible}')
print(f'Answer part 2: {max_score}')
