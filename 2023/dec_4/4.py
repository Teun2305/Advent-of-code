import re

with open('dec_4/4.in', 'r') as file:
    f = file.read().split('\n')

def get_numbers(line):
    line = line.split(':')[1].split('|')
    numbers = list()
    for n in line:
        numbers.append([int(number) for number in re.findall('\d+', n)])
    return numbers

total = 0

for line in f:
    w_numbers, c_numbers = get_numbers(line)
    points = len(set(w_numbers) & set(c_numbers))
    if points == 0:
        continue
    total += 2**(points - 1)

print(f'Answer 1 is {total}')

points = dict()
copies = dict()

for card, line in enumerate(f):
    w_numbers, c_numbers = get_numbers(line)
    points[card+1] = len(set(w_numbers) & set(c_numbers))
    copies[card+1] = 1

for card in points.keys():
    for i in range(card+1, card+points[card]+1):
        if i <= len(f):
            copies[i] += copies[card]

print(f'Answer 2 is {sum(copies.values())}')
