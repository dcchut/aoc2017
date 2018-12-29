from utils import load_input, get_numbers


def wrap_reverse(li, idx, length):
    if length > len(li):
        return []

    if idx + length < len(li):
        return li[:idx] + li[idx:idx+length][::-1] + li[idx+length:]
    else:
        # have some overflow
        overflow = length - (len(li) - idx)
        sublist = (li[idx:] + li[:overflow])[::-1]

        return sublist[len(li)-idx:] + li[overflow:idx] + sublist[:len(li)-idx]


numbers = list(range(256))
current_position = 0
skip_size = 0
lengths = get_numbers(load_input('puzzle_inputs/Day10.txt')[0])

for length in lengths:
    numbers = wrap_reverse(numbers, current_position % len(numbers), length)
    current_position += length + skip_size
    skip_size += 1

print('Part 1:', numbers[0] * numbers[1])

# PART 2
lengths = [ord(c) for c in load_input('puzzle_inputs/Day10.txt')[0]]
lengths.extend([17, 31, 73, 47, 23])

current_position = 0
skip_size = 0
numbers = list(range(256))

for round in range(64):
    for length in lengths:
        numbers = wrap_reverse(numbers, current_position % len(numbers), length)
        current_position += length + skip_size
        skip_size += 1

# xor & hex stage
hash = ''

for k in range(256//16):
    r = numbers[k*16]
    for p in numbers[k*16+1:(k+1)*16]:
        r = r ^ p
    h = hex(r)[2:]
    if len(h) == 1:
        h = '0' + h
    hash += h

print('Part 2:', hash)