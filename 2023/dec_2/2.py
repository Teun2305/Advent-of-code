with open('2.in', 'r') as file:
    f = file.read().split('\n')

possible = {
    'red': 12,
    'green' : 13,
    'blue' : 14
}

total = 0

for line in f:
    game_nr = int(line.split(':')[0].split()[1])

    for game in line.split(':')[1].split(';'):
        for cube in game.split(', '):
            amount, colour = cube.split()
            if int(amount) > possible.get(colour):
                game_nr = 0

    total += game_nr

print(f'Answer part 1 is {total}')

total = 0

for line in f:
    colours = {
            'red': 0,
            'green' : 0,
            'blue' : 0
        }
    
    for game in line.split(':')[1].split(';'):
        for cube in game.split(', '):
            amount, colour = cube.split()
            if int(amount) > colours.get(colour):
                colours[colour] = int(amount)

    total_game = 1

    for c in colours.values():
        total_game *= c

    total += total_game

print(f'Answer part 2 is {total}')