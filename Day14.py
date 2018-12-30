from utils import mapint
from Day10 import wrap_reverse
from cartesian import left, right, up, down

def hex_to_binary(h):
    if h == '0':
        return '0000'
    if h == '1':
        return '0001'
    if h == '2':
        return '0010'
    if h == '3':
        return '0011'
    if h == '4':
        return '0100'
    if h == '5':
        return '0101'
    if h == '6':
        return '0110'
    if h == '7':
        return '0111'
    if h == '8':
        return '1000'
    if h == '9':
        return '1001'
    if h == 'a':
        return '1010'
    if h == 'b':
        return '1011'
    if h == 'c':
        return '1100'
    if h == 'd':
        return '1101'
    if h == 'e':
        return '1110'
    if h == 'f':
        return '1111'


def knot_hash(word):
    lengths = [ord(c) for c in word]
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
    return hash


square_grid = set()
squares = 0

for k in range(128):
    binary = ''.join([hex_to_binary(q) for q in knot_hash(f'jxqlasbh-{k}')])
    for l,c in enumerate(binary):
        if c == '1':
            square_grid.add((l,k))

    squares += sum(mapint(binary))

print('Part 1:', squares)

regions = 0
while len(square_grid) > 0:
    p = square_grid.pop()
    queue = set([p])

    while len(queue) > 0:
        p = queue.pop()

        for q in [left(p),right(p),up(p),down(p)]:
            if q in square_grid:
                queue.add(q)
                square_grid.remove(q)
    regions += 1

print('Part 2:', regions)