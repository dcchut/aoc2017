from utils import load_input, Graph, GraphNode, Edge

def n(p):
    return (p[0]+0,p[1]+1,p[2]-1)


def s(p):
    return (p[0]+0,p[1]-1,p[2]+1)


def ne(p):
    return (p[0]+1,p[1],p[2]-1)


def se(p):
    return (p[0]+1,p[1]-1,p[2])


def nw(p):
    return (p[0]-1,p[1]+1,p[2])


def sw(p):
    return (p[0]-1,p[1],p[2]+1)


def shortest_path(p):
    return max(abs(p[0]),abs(p[1]),abs(p[2]))


# hexagonal grid
steps = load_input('puzzle_inputs/Day11.txt')[0].split(',')

current_position = (0,0,0)
sp_max = 0

for step in steps:
    c = f'current_position = {step}(current_position)'
    exec(c)
    sp = shortest_path(current_position)
    if sp > sp_max:
        sp_max = sp


target_position = current_position

print('Part 1:', shortest_path(target_position))
print('Part 2:', sp_max)