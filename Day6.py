from utils import get_numbers, load_input, constraint_max


def redistribute_blocks():
    # choose the bank with the highest number of blocks
    max_bank = constraint_max(banks, lambda q: banks[q], lambda q: -q)

    wealth = banks[max_bank]
    banks[max_bank] = 0

    current_bank = (max_bank + 1) % len(banks)

    while wealth > 0:
        banks[current_bank] += 1
        current_bank = (current_bank + 1) % len(banks)
        wealth -= 1


puzzle_input = load_input('puzzle_inputs/Day6.txt')

banks = {}
for (k,line) in enumerate(get_numbers(puzzle_input[0])):
    banks[k] = int(line)

bank_state = tuple(banks.values())
visited = set()
seen_at = {}
steps = 0

while bank_state not in visited:
    seen_at[bank_state] = steps
    visited.add(bank_state)
    redistribute_blocks()
    bank_state = tuple(banks.values())
    steps += 1

print('Part 1:',len(visited))
print('Part 2:',steps-seen_at[bank_state])
