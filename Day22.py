from utils import load_input
from collections import defaultdict
from cartesian import left, right, up, down, turn_left, turn_right


grid = defaultdict(int)
puzzle_input = load_input('puzzle_inputs/Day22.txt')

for (y,line) in enumerate(puzzle_input):
    for (x, char) in enumerate(line):
        if char == '#':
            grid[(x,y)] = 1

# initially start at the centre of our input, facing up
pos = (len(puzzle_input)//2,len(puzzle_input)//2)
direction = up

burst = 0
infections = 0
while burst < 10000:
    x, y = pos
    if grid[(x,y)] == 1:
        direction = turn_right(direction)
    else:
        infections += 1
        direction = turn_left(direction)

    grid[(x,y)] = 1 - grid[(x,y)]
    pos = direction(pos)
    burst += 1

print('Part 1:', infections)

grid = defaultdict(int)

for (y, line) in enumerate(puzzle_input):
    for (x, char) in enumerate(line):
        if char == '#':
            grid[(x, y)] = 2 # infected is now 2

pos = (len(puzzle_input) // 2, len(puzzle_input) // 2)
direction = up
burst = 0
infections = 0

# clean = 0
# weakened = 1
# infected = 2
# flagged = 3

while burst < 10000000:
    x, y = pos

    # change direction phase
    if grid[pos] == 0:
        direction = turn_left(direction)
    elif grid[pos] == 1:
        infections += 1
    elif grid[pos] == 2:
        direction = turn_right(direction)
    elif grid[pos] == 3:
        direction = turn_right(turn_right(direction)) # reverse direction

    # change infesction state phase
    grid[pos] = (grid[pos] + 1) % 4

    # move phase
    pos = direction(pos)
    burst += 1

print('Part 2:', infections)
