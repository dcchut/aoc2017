from utils import load_input

puzzle_input = load_input('puzzle_inputs/Day9.txt')[0]

idx = 0
in_garbage = False
level = 0
scores = {0 : 0}
score_total = 0
garbage_counter = 0

while idx < len(puzzle_input):
    char = puzzle_input[idx]

    if in_garbage:
        if char == '!':
            idx += 1
        elif char == '>':
            in_garbage = False
        else:
            garbage_counter += 1
    else:
        if char == '<':
            # start garbage!
            in_garbage = True
        if char == '{':
            # add the parent score + 1 to the total score,
            # and then remember what this score is for our children
            score_total += scores[level] + 1
            scores[level+1] = scores[level]+1
            level += 1
        if char == '}':
            level -= 1

    idx += 1

print('Part 1:', score_total)
print('Part 2:', garbage_counter)




