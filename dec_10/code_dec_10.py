with open('input_dec_10.txt') as file:
    f = file.readlines()
'''X = 1
iteration = 0
signal = [i for i in range(20, 121, 20)]
signal_strength = list()'''




class CPU:
    def __init__(self):
        self.X = 1
        self.iter = 0
        self.strength = 0
        self.image = ''

    def next_iter(self, cycles, V=0):
        for _ in range(cycles):
            if abs(self.iter % 40 - self.X) <= 1:
                self.image += '#'
            else:
                self.image += '.'
            if (self.iter + 1) % 40 == 0:
                self.image += '\n'

            self.iter += 1
            if (self.iter - 20) % 40 == 0:
                self.strength += self.X * self.iter

        self.X += V

cpu = CPU()

for line in f:
    line = line.strip('\n')
    if line == 'noop':
        cpu.next_iter(1)
    elif 'addx' in line:
        cpu.next_iter(2, V=int(line.split()[1]))
    else:
        raise ValueError

print(f'Answer part 1: {cpu.strength}')
print(f'Answer part 2: RZHFGJCB\n{cpu.image}')