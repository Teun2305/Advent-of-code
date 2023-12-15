import re

with open('dec_6/6.in', 'r') as file:
    f = file.read().split('\n')

times = [int(t) for t in re.findall('\d+', f[0])]
dists = [int(d) for d in re.findall('\d+', f[1])]

total = 1
for t, d in zip(times, dists):
    counter = 0
    for i in range(t):
        if i * (t - i) > d:
            counter += 1
    total *= counter

print(f'Answer 1 is {total}')

time = dist = ''
for t, d in zip(times, dists):
    time += str(t)
    dist += str(d)
time, dist = int(time), int(dist)

total = 0

for i in range(time):
    if i * (time - i) > dist:
        total += 1

print(f'Answer 2 is {total}')
