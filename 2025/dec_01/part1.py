FILENAME = "2025/dec_01/in.txt"

rotations = []
with open(FILENAME, "r") as file:
    for line in file:
        direction = line[0]
        amount = int(line[1:])
        rotations.append((direction, amount))

position = 50
password = 0

for direction, amount in rotations:
    if direction == "R":
        position = (position + amount) % 100
    else:
        position = (position - amount) % 100

    if position < 0:
        position += 100
    elif position == 0:
        password += 1

print(password)