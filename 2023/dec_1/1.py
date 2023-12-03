import re

with open('dec_1/1.in', 'r') as file:
    f = file.read()

total1 = 0
total2 = 0

digits = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight': 8,
    'nine' : 9
}

for line in f.split('\n'):
    number = ''.join(re.findall('\d', line))
    if number == '':
        continue
    total1 += int(number[0] + number[-1])

print(f'Answer 1 is {total1}')

digits_str = '|'.join(digits.keys())

for line in f.split('\n'):
    number = re.findall(f'\d|{digits_str}', line)
    number = list(filter(lambda x: x != '', number))

    for i, n in enumerate(number):
        if n in digits.keys():
            number[i] = str(digits.get(n))

    total2 += int(number[0] + number[-1])

    

print(f'Answer 2 is {total2}')