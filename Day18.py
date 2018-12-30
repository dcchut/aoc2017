from utils import load_input
from collections import defaultdict


def value(y):
    if y.isalpha():
        return registers[y]
    else:
        return int(y)


puzzle_input = load_input('puzzle_inputs/Day18.txt')
registers = defaultdict(int)
last_snd = None

k = -1
while False and k < len(puzzle_input):
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
        elif operation == 'add':
            registers[x] += value(y)
        elif operation == 'mul':
            registers[x] *= value(y)
        elif operation == 'mod':
            registers[x] = registers[x] % value(y)
        elif operation == 'jgz':
            if registers[x] > 0:
                k += value(y) - 1


def valuecp(y, cp):
    if type(y) == int:
        return y
    if y.isalpha():
        return registers[cp][y]
    else:
        return int(y)


puzzle_input = load_input('puzzle_inputs/Day18.txt')
registers = [defaultdict(int),defaultdict(int)]
registers[0]['p'] = 0
registers[1]['p'] = 1
current_program = 0
queues = {0 : [], 1 : []}
last_snd = None
last_operation = None
c = 0
k = [-1,-1]
banned = set()
steps = 0
while True:
    steps += 1
    k[current_program] += 1
    if len(banned) == 2:
        print('Invalid memory access')
        break
    elif k[current_program] >= len(puzzle_input):
        banned.add(current_program)
        current_program = (current_program + 1) % 2



    line = puzzle_input[k[current_program]].split()
    operation = line[0]

    if operation == 'snd':
        if current_program == 0:
            c += 1
        queues[(current_program + 1) % 2].append(valuecp(line[1],current_program))
    elif operation == 'rcv':
        x = line[1]
        # we can consume immediately!
        if len(queues[current_program]) > 0:
            top = queues[current_program].pop(0)
            registers[current_program][x] = top
            last_operation = None
        else:
            if operation == last_operation:
                print('Deadlock')
                break
            k[current_program] -= 1
            # we have to wait - switch contexts
            current_program = (current_program + 1) % 2

    else:
        x = line[1]
        y = line[2]

        if operation == 'set':
            registers[current_program][x] = valuecp(y,current_program)
        elif operation == 'add':
            registers[current_program][x] += valuecp(y,current_program)
        elif operation == 'mul':
            registers[current_program][x] *= valuecp(y,current_program)
        elif operation == 'mod':
            registers[current_program][x] %= valuecp(y,current_program)
        elif operation == 'jgz':
            if valuecp(x,current_program) > 0:
                k[current_program] += valuecp(y,current_program) - 1
    last_operation = operation

print(c)