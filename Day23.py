from utils import load_input
from collections import defaultdict


def value(y):
    if type(y) == int:
        return y
    if y.isalpha():
        return registers[y]
    else:
        return int(y)


puzzle_input = load_input('puzzle_inputs/Day23.txt')
registers = defaultdict(int)
last_snd = None

k = -1
mul = 0

while -1 <= k < len(puzzle_input)-1:
    k += 1
    line = puzzle_input[k].split()
    operation = line[0]

    if operation == 'snd':
        last_snd = value(line[1])
    elif operation == 'rcv':
        x = line[1]
        if value(x) != 0:
            print('RCV:', last_snd)
            break
    else:
        x = line[1]
        y = line[2]

        if operation == 'set':
            registers[x] = value(y)
        elif operation == 'sub':
            registers[x] -= value(y)
        elif operation == 'add':
            registers[x] += value(y)
        elif operation == 'mul':
            mul += 1
            registers[x] = registers[x] * value(y)
        elif operation == 'mod':
            registers[x] = registers[x] % value(y)
        elif operation == 'jnz':
            if value(x) != 0:
                k += value(y) - 1

print('Part 1:', mul)

registers = defaultdict(int)
b = 67*100 + 100000
c = b + 17000

count = 0
for i in range(b,c+1,17):
    for j in range(2,i):
        if j**2 > i:
            break
        if i % j == 0:
            count += 1
            break

print('Part 2:', count)