import re

with open('dec_5/5.in', 'r') as file:
    f = file.read().split('\n\n')

def in_range(number, first, length):
    return first <= number < first + length

def get_next(seed, map):
    for des, source, length in map:
        if in_range(seed, source, length):
            return des + seed - source
    return seed


seeds = [int(seed) for seed in re.findall('\d+', f[0])]

maps = list()

for block in f[1:]:
    line = block.split('\n')
    map = list()
    for numbers in line[1:]:
        map.append(tuple([int(n) for n in re.findall('\d+', numbers)]))
    maps.append(map)

locations = list()

for seed in seeds:
    for map in maps:
        seed = get_next(seed, map)
    locations.append(seed)

print(f'Answer 1 is {min(locations)}')

locations = list()
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

for i, (seed, length) in enumerate(seeds):
    for s in range(seed, seed+length):
        for map in maps:
            s = get_next(s, map)
        locations.append(s)
    print(f'{100*(i+1)/len(seeds)}%')

print(f'Answer 2 is {min(locations)}')
