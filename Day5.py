from utils import load_input

puzzle_input = load_input('puzzle_inputs/Day5.txt')

pointer = 0
steps = 0
offsets = [int(line) for line in puzzle_input]

while pointer < len(offsets):
    old_pointer = pointer
    pointer += offsets[pointer]
    offsets[old_pointer] += 1
    steps += 1

print('Part 1:', steps)

pointer = 0
steps = 0
offsets = [int(line) for line in puzzle_input]

while pointer < len(offsets):
    old_pointer = pointer
    pointer += offsets[pointer]
    if offsets[old_pointer] >= 3:
        offsets[old_pointer] -= 1
    else:
        offsets[old_pointer] += 1
    steps += 1

print('Part 2:', steps)