FILENAME = "2025/dec_03/in.txt"

with open(FILENAME, "r") as file:
    banks = [bank.strip() for bank in file.readlines()]

total_joltage = 0

for bank in banks:
    jolt1 = bank.index(max(bank[:-1]))
    jolt2 = max(bank[jolt1+1:])
    total_joltage += int(bank[jolt1] + jolt2)

print(total_joltage)
