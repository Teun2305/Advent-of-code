FILENAME = "2025/dec_03/in.txt"

with open(FILENAME, "r") as file:
    banks = [bank.strip() for bank in file.readlines()]

total_joltage = 0
joltage_size = 12

for bank in banks:
    jolts = [-1]
    for i in range(joltage_size):
        jolts.append(bank.index(max(bank[jolts[i]+1:len(bank)-joltage_size+i+1]), jolts[i]+1))
    
    total_joltage += int("".join([bank[jolt] for jolt in jolts[1:]]))

print(total_joltage)
