from queue import Queue

with open('input_dec_11.txt', 'r') as file:
    f = file.read().split('\n\n')

class Monkey:
    def __init__(self, items, operation, v, divisible, new_monkeys):
        self.items = items
        self.operation, self.v = operation, v
        self.divisible = divisible
        self.t, self.f = new_monkeys
        self.inspections = 0


    def inspection(self, part1, div):
        self.inspections += len(self.items)
        while len(self.items) > 0:
            item = self.items.pop(0)

            if part1:
                if self.v == 'old':
                    item = self.operation(item, item) // 3
                else:
                    item = self.operation(item, self.v) // 3
            else:
                if self.v == 'old':
                    item = self.operation(item, item) % div
                else:
                    item = self.operation(item, self.v) % div
            
            if item % self.divisible == 0:
                monkeys[self.t].items.append(item)
            else:
                monkeys[self.f].items.append(item)


    def __str__(self):
        string = f'items: '
        for item in self.items:
            string += str(item) + ' '
        string += f'\nv: {self.v}\n'
        string += f'divisible: {self.divisible}\n'
        string += f't, f: {self.t}, {self.f}\n\n'
        return string
    

operators = {
    '+' : lambda old, v: old + v,
    '*' : lambda old, v: old * v
}
monkeys = dict()
dividers = list()

def monkeys_reset(monkey_file):
    for line in monkey_file:
        line = [l.strip() for l in line.split('\n')]
        number = int(line[0][-2])
        items = [int(item) for item in line[1][16::].split(',')]
        operation, v = operators[line[2][21:22:]], line[2][23::]
        try:
            v = int(v)
        except ValueError:
            pass

        divisible = int(line[3][19::])
        dividers.append(divisible)
        new_monkeys = int(line[4][25::]), int(line[5][26::])

        monkeys[number] = Monkey(items, operation, v, divisible, new_monkeys)

def rounds(n, part1):
    monkeys_reset(f)
    div = 1
    for d in dividers:
        div *= d
        
    for i in range(n):
        for monkey in monkeys.values():
            monkey.inspection(part1, div)
    
    business = list(map(lambda m: m.inspections, monkeys.values()))
    business.sort()
    return business[-1] * business[-2]


print(f'Answer part 1: {rounds(20, True)}')
print(f'Answer part 2: {rounds(10_000, False)}')
