with open('input_dec_7.txt') as file:
    f = [line.strip('\n') for line in file.readlines()]

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content = list()

    def is_empty(self):
        return len(self.content) == 0

    def get_size(self):
        return sum(list(map(lambda x: x.get_size(), self.content)))
        

class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name

    def get_size(self):
        return self.size


cur_dir = Directory('/', None)
directories = [cur_dir]

def find_dir(name):
    for item in cur_dir.content:
        if item.name == name:
            return item


for i, line in enumerate(f):
    commands = line.split()
    if commands[0] == '$' and commands[1] == 'cd':
        if commands[2] == '..':
            cur_dir = cur_dir.parent
        elif i > 0:
            cur_dir = find_dir(commands[2])
    
    elif commands[0] == '$':
        continue

    elif commands[0] == 'dir':
        dir = Directory(commands[1], cur_dir)
        cur_dir.content.append(dir)
        directories.append(dir)

    else:
        cur_dir.content.append(File(commands[0], commands[1]))

directories.sort(key=lambda x: x.get_size())
available_space = 70_000_000 - directories[-1].get_size()
needed_space = 30_000_000 - available_space

total_size = 0
size_smallest_dir = 0
for dir in directories:
    size = dir.get_size()
    if size <= 100_000:
        total_size += size
    if size >= needed_space:
        size_smallest_dir = size
        break

print(f'Answer part 1: {total_size}')
print(f'Answer part 2: {size_smallest_dir}')
