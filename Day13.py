from utils import load_input, get_numbers, memoize
from collections import defaultdict
import z3


# Part 1
def compute_intersections(delay):
    layers = defaultdict(int)
    layer_state = {}
    layer_down = {}

    for line in load_input('puzzle_inputs/Day13.txt'):
        depth, length = get_numbers(line)

        layers[depth] = length
        layer_state[depth] = 0
        layer_down[depth] = True

    intersections = 0

    for s in range(max(layers.keys()) + 1 + delay):
        if s - delay >= 0:
            if layers[s - delay] > 0:
                # actually have a layer here
                # are we touching a scanner?
                if layer_state[s - delay] == 0:
                    intersections += (s - delay) * layers[s - delay]

        # move all of the scanners
        for d in layers:
            if layers[d] > 0:
                if layer_state[d] == layers[d] - 1 and layer_down[d]:
                    layer_down[d] = False
                    layer_state[d] -= 1
                elif layer_state[d] == 0 and not layer_down[d]:
                    layer_down[d] = True
                    layer_state[d] += 1
                elif layer_down[d]:
                    layer_state[d] += 1
                else:
                    layer_state[d] -= 1

    return intersections


print('Part 1:', compute_intersections(0))

# PART 2
layers = {}
for line in load_input('puzzle_inputs/Day13.txt'):
    depth, length = get_numbers(line)
    layers[depth] = length

delay = 0
while True:
    found = True

    for d in layers:
        if ((d + delay) % (2 * layers[d] - 2) == 0):
            found = False
            break

    if found:
        break

    delay += 1

print('Part 2:', delay)



# this solution didn't turn out to be quick enough to compute in a reasonable amount of time
#o = z3.Optimize()
#
#layers = defaultdict(int)
#layer_state = {}
#layer_down = {}
#intersections = {}
#
#delay = z3.Int('delay')
#
#for line in load_input('puzzle_inputs/Day13.txt'):
#    depth, length = get_numbers(line)
#
#    layers[depth] = length
#    layer_state[depth] = 0
#    layer_down[depth] = True
#
#    # add a variable for whether there'll be an intersection with this layer
#    # at time s (=depth) + delay d
#    intersections[depth] = z3.Bool(f"intersection_{depth}")
#    o.add(intersections[depth] == z3.If((depth + delay) % (2 * length - 2) == 0, False, True))
#
#p = z3.And(*list(intersections.values()))
#o.add(p)
#o.add(delay >= 0)
#
#h2 = o.minimize(delay)
#
#o.check()
#print(o.model())
#print(h2.lower())
