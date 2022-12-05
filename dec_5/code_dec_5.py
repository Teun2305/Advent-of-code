# Note that the input is not the same as provided by Advent of Code. 2 lines have been deleted.
with open('input_dec_5.txt', 'r') as file:
    commands = list()
    for i, x in enumerate(file):
        if i == 0:
            n_stacks = len(x) // 4
            stacks1= [list() for _ in range(n_stacks)]

        if x[:4:] == 'move':
            line = x.split()
            commands.append((int(line[1]), int(line[3])-1, int(line[5])-1))

        else:
            for j, s in enumerate(stacks1):
                ind = 1+j*4
                item = x[ind:ind+1:]
                if item != ' ':
                    s.append(item)

stacks2 = [s.copy() for s in stacks1]

for amount, source, target in commands:
    for i in range(amount):
        item1 = stacks1[source].pop(0)
        stacks1[target].insert(0, item1)

        item2 = stacks2[source].pop(amount-i-1)
        stacks2[target].insert(0, item2)
    
answer1 = ''.join([s[0] for s in stacks1])
print(f'Answer part 1: {answer1}')

answer2 = ''.join([s[0] for s in stacks2])
print(f'Answer part 2: {answer2}')
