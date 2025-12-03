FILENAME = "2025/dec_02/in.txt"

ranges = []
with open(FILENAME, "r") as file:
    for full_range in file.read().split(","):
        start, end = full_range.split("-")
        ranges.append((int(start), int(end)))

invalid_id = set()

for start, end in ranges:
    for i in range(start, end+1):
        str_i = str(i)
        for j in range(1, len(str_i) // 2 + 1):
            count = str_i.count(str_i[:j])
            if count > 1 and len(str_i) - len(str_i[:j]) * count == 0:
                invalid_id.add(i)


print(sum(invalid_id))