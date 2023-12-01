with open('dec_15/in15.txt', 'r') as file:
    f = file.read().split('\n')

class Grid:
    def __init__(self, sensors, beacons):
        self.max_col, self.max_row = float('-inf'), float('-inf')
        self.min_col, self.min_row = float('inf'), float('inf')
        self.sensors = sensors
        self.beacons = beacons
        self.set_min_max()
        self.distances = list()
        self.set_distances()

    def set_min_max(self):
        for s, b in zip(self.sensors, self.beacons):
            sx, sy = s
            bx, by = b
            if sx > self.max_col:
                self.max_col = sx
            if sx < self.min_col:
                self.min_col = sx
            if bx > self.max_col:
                self.max_col = bx
            if bx < self.min_col:
                self.min_col = bx

            if sy > self.max_row:
                self.max_row = sy
            if sy < self.min_row:
                self.min_row = sy
            if by > self.max_row:
                self.max_row = by
            if by < self.min_row:
                self.min_row = by
                            
    def set_distances(self):
        for s, b in zip(self.sensors, self.beacons):
            x1, y1 = s
            x2, y2 = b
            self.distances.append(self.manhattan(x1, y1, x2, x2))

    def manhattan(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def beacon_present(self, col, row):
        if (col, row) in self.beacons:
            return False
        for s, b in zip(self.sensors, self.beacons):
            s_col, s_row = s
            b_col, b_row = b
            sb_dist = self.manhattan(s_col, s_row, b_col, b_row)
            s_dist = self.manhattan(s_col, s_row, col, row)
            if s_dist <= sb_dist:
                #print(f'this = ({col}, {row}) - S: {s} - B: {b}')
                #print(f'sb: {sb_dist} - s: {s_dist}')
                return True
        
        return False

    def count(self, row):
        counter = 0
        dist = max(self.distances)
        for col in range(self.min_col-dist, self.max_col+dist+1):
            if self.beacon_present(col, row):
                counter += 1

        return counter



sensors = list()
beacons = list()
for line in f:
    line = line.replace('Sensor at ', '')
    line = line.replace('=', '')
    line = line.replace(',', '')
    line = line.replace('x', '')
    line = line.replace('y', '')
    line = line.replace(': closest beacon is at ', ' ')
    sx, sy, bx, by = [int(x) for x in line.split()]
    sensors.append((sx, sy))
    beacons.append((bx, by))


min_x, min_y = float('inf'), float('inf')
max_x, max_y = float('-inf'), float('-inf')

g = Grid(sensors, beacons)
print(f'Answer part 1: {g.count(2_000_000)}')

# Technically works, but takes far too long to actually execute
n = 4_000_000
for col in range(n):
    for row in range(n):
        if not g.beacon_present(col, row) and not (col, row) in beacons:
            print(f'Answer part 2: {col*n + row}')



