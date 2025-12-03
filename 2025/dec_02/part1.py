FILENAME = "2025/dec_02/in.txt"

ranges = []
with open(FILENAME, "r") as file:
    for full_range in file.read().split(","):
        start, end = full_range.split("-")
        ranges.append((int(start), int(end)))

sum_id = 0

for start, end in ranges:
    for i in range(start, end+1):
        str_i = str(i)
        half = len(str_i) // 2
        if str_i[:half] == str_i[half:]:
            sum_id += i

print(sum_id)