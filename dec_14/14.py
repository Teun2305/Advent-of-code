with open('dec_14/in14.txt', 'r') as file:
    f = file.readlines()

class Grid:
    def __init__(self, max_x, min_x, y):
        self.grid = [['.' for _ in range(max_x-min_x+2*y)] for _ in range(y+2)]
        self.min_x, self.max_x = min_x, max_x
        self.y = y
        self.grid[0][self.ind(500)] = '+'
        self.grid.append(['#' for _ in range(max_x-min_x+2*y)])

    def ind(self, col):
        return col - self.min_x + self.y

    def get_direction(self, diff_x, diff_y):
        x, y = 0, 0
        if diff_x > 0:
            x = 1
        elif diff_x < 0:
            x = -1
        if diff_y > 0:
            y = 1
        elif diff_y < 0:
            y = -1
        return x, y

    def add_rocks(self, path):
        for p1, p2 in zip(path, path[1::]):
            x1, y1 = p1
            x2, y2 = p2
            diff_x = x2 - x1
            diff_y = y2 - y1
            length = abs(diff_x + diff_y) + 1
            x, y = self.get_direction(diff_x, diff_y)
            for _ in range(length):
                self.grid[y1][self.ind(x1)] = '#'
                x1 += x
                y1 += y

    def add_sand(self):
        row, col = 0, 500
        changed = True
        void = False
        while changed and not void:
            try:
                if self.grid[row+1][self.ind(col)] == '.':
                    row += 1
                elif self.grid[row+1][self.ind(col)-1] == '.':
                    row += 1
                    col -= 1
                elif self.grid[row+1][self.ind(col)+1] == '.':
                    row += 1
                    col += 1
                elif row == 0 and col == 500:
                    void = True
                else:
                    changed = False
            except IndexError:
                void = True

        self.grid[row][self.ind(col)] = 'o'
        return void

    def count_sand(self, part1):
        counter = 0
        for row in self.grid:
            for field in row:
                if field == 'o':
                    counter += 1
        return counter

    def __str__(self):
        string = ''
        for row in self.grid:
            string += ' '.join(row) + '\n'
        return string


paths = list()
for line in f:
    path = list()
    line = line.strip('\n')
    coords = line.split(' -> ')
    for coord in coords:
        x, y = coord.split(',')
        path.append((int(x), int(y)))
    paths.append(path)

min_x = float('inf')
max_x, max_y = float('-inf'), float('-inf')

for path in paths:
    for coord in path:
        x, y = coord
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x
        elif x < min_x:
            min_x = x

g = Grid(max_x, min_x, max_y)
for path in paths:
    g.add_rocks(path)
void = False
while not void:
    void = g.add_sand()

#print(f'Answer part 1: {g.count_sand()}')
print(f'Answer part 2: {g.count_sand()}')

