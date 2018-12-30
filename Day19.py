from utils import load_input
from cartesian import left, right, up, down

def b(pos):
    if pos[1] < 0 or pos[1] >= len(puzzle_input) or pos[0] < 0 or pos[0] >= len(puzzle_input[pos[1]]):
        return ' '
    return puzzle_input[pos[1]][pos[0]]


puzzle_input = load_input('puzzle_inputs/Day19.txt')

pos = (puzzle_input[0].index('|'),0)
direction = down

word = ''
steps = 1

while True:
    # if we're on a letter, add it to our word
    if b(pos).isalpha():
        word += b(pos)

    dpos = direction(pos)
    # if we're ok to move in our current direction, then do so
    if b(dpos) != ' ':
        pos = direction(pos)
        steps += 1
    else:
        # otherwise, change directions
        if direction in [left, right]:
            if b(up(pos)) != ' ':
                direction = up
            elif b(down(pos)) != ' ':
                direction = down
            else:
                # no way to turn - we're at the end
                break
        else:
            if b(left(pos)) != ' ':
                direction = left
            elif b(right(pos)) != ' ':
                direction = right
            else:
                break

print('Part 1:', word)
print('Part 2:', steps)