with open('dec_13/in13.txt', 'r') as file:
    f = file.read().split('\n')

for _ in range(len(f)//3):
    f.remove('')

def get_packet(line):
    line = split(line[1:-1:])
    packet = list()
    for element in line:
        if isinstance(element, int):
            packet.append(element)
        else:
            packet.append(get_packet(element))

    return packet

def split(line):
    split_list = list()
    depth = 0
    string = ''
    for element in line:
        if depth > 0:
            string += element
            if element == '[':
                depth += 1
            elif element == ']' and depth == 1:
                split_list.append(string)
                depth -= 1
                string = ''
            elif element == ']':
                depth -= 1
        elif element == ',':
            if len(string) > 0:
                split_list.append(int(string))
                string = ''
        elif element == '[':
            string += element
            depth += 1
        else:
            string += element

    if len(string) > 0:
        split_list.append(int(string))
    return split_list

def compare(l, r):
    left, right = l.copy(), r.copy()

    while len(left) > 0 and len(right) > 0:
        if isinstance(left[0], int) and isinstance(right[0], int):
            if left[0] == right[0]:
                del left[0]
                del right[0]
                continue
            else:
                return right[0] > left[0]
                

        if isinstance(left[0], int):
            left[0] = [left[0]]
        elif isinstance(right[0], int):
            right[0] = [right[0]]

        bool = compare(left[0], right[0])
        if bool is None:
            del left[0]
            del right[0]
            continue
        else:
            return bool

    if len(left) == 0 and len(right) == 0:
        return None
    else:
        return len(left) == 0

packets = list(map(lambda x: get_packet(x), f))

indices = list()
for i, (packet1, packet2) in enumerate(zip(packets[::2], packets[1::2])):
    if compare(packet1, packet2):
        indices.append(i+1)

packets.append([[2]])
packets.append([[6]])
print([[2]] in packets)

l = len(packets) - 1
for _ in range(l):
    for j in range(l):
        if not compare(packets[j], packets[j+1]):
            packets[j], packets[j+1] = packets[j+1], packets[j]

answer2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
print(f'Answer part 1: {sum(indices)}')
print(f'Answer part 2: {answer2}')



