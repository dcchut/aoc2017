from utils import load_input, get_numbers
from collections import defaultdict

#Begin in state A.
#Perform a diagnostic checksum after 12586542 steps.

rules = defaultdict(dict)

for (k, line) in enumerate(load_input('puzzle_inputs/Day25.txt')):
    s = line.split()
    if k % 10 == 0:
        state = line[-2]
    if k % 10 in [1,5]:
        cv = get_numbers(line)[0]
    if k % 10 in [2,6]:
        wr = get_numbers(line)[0]
    if k % 10 in [3,7]:
        if line.strip()[-5:] == 'left.':
            move = -1
        else:
            move = 1
    elif k % 10 in [4,8]:
        target_state = line[-2]
        rules[state][cv] = (wr, move, target_state)

state = 'A'
tape = defaultdict(int)
current_tape_position = 0

steps = 0
while steps < 12586542:
    wr, move, target_state = rules[state][tape[current_tape_position]]
    tape[current_tape_position] = wr
    current_tape_position += move
    state = target_state
    steps += 1

print('Part 1:', sum(list(tape.values())))