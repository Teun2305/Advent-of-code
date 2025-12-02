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
    password += amount // 100
    amount = amount % 100
    zero_start = position == 0

    if direction == "R":
        position += amount
    else:
        position -= amount
    
    if position < 0:
        position += 100
        password += 1
        if zero_start and direction == "L":
            password -= 1
    elif position >= 100:
        position -= 100
        password += 1
    elif position == 0:
        password += 1
        
print(password)
