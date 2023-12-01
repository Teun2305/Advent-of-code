with open('dec_16/in16.txt', 'r') as file:
    f = file.read().split('\n')

class Valve:
    def __init__(self, name, rate, neighbours):
        self.name = name
        self.rate = int(rate)
        self.neighbours = neighbours
        self.opened = False

    def set_neighbours(self, valves):
        self.neighbours = list(map(lambda n: self.neighbour(n, valves), self.neighbours))
        self.neighbours.sort(key=lambda n: n.rate, reverse=True)

    def neighbour(self, name, valves):
        for v in valves:
            if name == v.name:
                return v

    def __eq__(self, other):
        if not isinstance(other, Valve):
            return False
        return self.name == other.name

    def __str__(self):
        return f'Name: {self.name} -- Rate: {self.rate} -- Neighbours: {[n.name for n in self.neighbours]}'

def get_flow(valves):
    open_valves = list(filter(lambda v: v.opened, valves))
    return sum(list(map(lambda v: v.rate, open_valves)))

valves = list()
for line in f:
    line = line.replace('Valve ', '')
    line = line.replace(' has flow rate=', '|')
    line = line.replace('; tunnels lead to valves ', '|')
    line = line.replace('; tunnel leads to valve ', '|')
    name, rate, neighbours = line.split('|')
    neighbours = neighbours.split(', ')
    valves.append(Valve(name, rate, neighbours))

for valve in valves:
    valve.set_neighbours(valves)
    print(valve)

flow = 0
minutes = 30
for _ in range(minutes):
