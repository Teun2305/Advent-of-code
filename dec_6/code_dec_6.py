with open('input_dec_6.txt', 'r') as file:
    line = file.readlines()[0]

def find_distict_sequence(l):
    for i, letter in enumerate(line[l-1::]):
        j = i + 4
        if len(set([x for x in line[j-l:j:]])) == l:
            return j
            break
    
print(f'Answer part 1: {find_distict_sequence(4)}')
print(f'Answer part 2: {find_distict_sequence(14)}')
