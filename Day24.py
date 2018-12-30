from utils import load_input, get_numbers, Graph, GraphNode, parallel_map, flatten_list
import sys
from collections import defaultdict

puzzle_input = load_input('puzzle_inputs/Day24.txt')

components = defaultdict(set)


def generate_bridges(bridge, components):
    if bridge is None:
        bridge = [(0,0)]

    cur = bridge[-1][1]

    bridges = []

    for b in components[cur]:
        if not ((cur,b) in bridge or (b,cur) in bridge):
            new_bridge = bridge + [(cur,b)]
            bridges.append(new_bridge)
            bridges.extend(generate_bridges(new_bridge,components))

    return bridges

for line in puzzle_input:
    x,y = get_numbers(line)

    components[x].add(y)
    components[y].add(x)

bridges = generate_bridges(None, components)
bridge_lengths = defaultdict(list)
for bridge in bridges:
    bridge_lengths[len(bridge)].append(sum(sum(n) for n in bridge))


print('Part 1:', max(sum(sum(n) for n in bridge) for bridge in bridges))
print('Part 2:', max(bridge_lengths[max(bridge_lengths)]))