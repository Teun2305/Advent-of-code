with open('input_dec_9.txt') as file:
    f = file.readlines()

class Rope:
    def __init__(self, parent=None):
        self.x, self.y = 0, 0
        self.visited = [(0, 0)]
        self.parent = parent

    def set_parent(self, parent):
        self.parent = parent

    def move(self, dir):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1
        else:
            raise ValueError
        
        self.visited.append((self.x, self.y))


    def in_range(self):
        return abs(self.x - self.parent.x) <= 1 and \
            abs(self.y - self.parent.y) <= 1


    def follow(self):
        dif_x = self.parent.x - self.x
        dif_y = self.parent.y - self.y
        if self.parent.x == self.x or self.parent.y == self.y:
            self.x += dif_x // 2
            self.y += dif_y // 2
            
        elif (dif_x == 2 and dif_y == 1) or (dif_x == 1 and dif_y == 2):
            self.x += 1
            self.y += 1
        elif (dif_x == -2 and dif_y == 1) or (dif_x == -1 and dif_y == 2):
            self.x -= 1
            self.y += 1
        elif (dif_x == -2 and dif_y == -1) or (dif_x == -1 and dif_y == -2):
            self.x -= 1
            self.y -= 1
        elif (dif_x == 2 and dif_y == -1) or (dif_x == 1 and dif_y == -2):
            self.x += 1
            self.y -= 1
        else:
            print_info()
            raise ValueError

        self.visited.append((self.x, self.y))


    def get_number_locations(self):
        return len(set(self.visited))

h, t = Rope(), Rope()
t.set_parent(h)

knots = [Rope() for _ in range(9)]
knots[0].set_parent(h)
for k1, k2 in zip(knots, knots[1::]):
    k2.set_parent(k1)

def print_info():
    print(f'h: {h.x} {h.y}')
    for i, k in enumerate(knots):
        print(f'{i}: {k.x} {k.y}')

for line in f:
    dir, amount = line.split()
    amount = int(amount.strip('\n'))
    print(dir, amount)
    for _ in range(amount): 
        h.move(dir)
        '''if not t.in_range():
            t.follow()'''
        
        for i, k in enumerate(knots):
            if not k.in_range():
                k.follow()

print(f'Answer part 1: {t.get_number_locations()}')
print(f'Answer part 2: {knots[-1].get_number_locations()}')
