from utils import get_numbers, load_input, Graph, GraphNode, Edge
from collections import Counter

def get_or_create_node(program_name, weight=None):
    if program_name not in noded:
        n = GraphNode(weight)
        g.add_node(n)
        noded[program_name] = n
    elif weight is not None:
        noded[program_name].data = weight
    return noded[program_name]


def tree_sum(node):
    s = 0

    nodes = set([node])

    while len(nodes) > 0:
        node = nodes.pop()
        s += node.data

        for next_node in g.get_neighbours(node):
            nodes.add(next_node)

    return s


noded = {}
puzzle_input = load_input('puzzle_inputs/Day7.txt')
g = Graph()

programs = set()
targets = set()

# parse puzzle input into a graph
for line in puzzle_input:
    program_name = line.split()[0]
    programs.add(program_name)
    weight = get_numbers(line)[0]
    n = get_or_create_node(program_name, weight)

    if '-> ' not in line:
        continue

    sline = line.split('-> ')[1].split(', ')
    for p in sline:
        child_node = get_or_create_node(p)
        e = Edge(n,child_node)
        g.add_edge(e)

        targets.add(p)


# start at the bottom until we find the first node that isn't misbalanced
# to balance everything out, we have to change the parent node of this node
bottom = programs.difference(targets).pop()
current_node = get_or_create_node(bottom)
balancer = None

print('Part 1:', bottom)

while current_node is not None:
    wrong_part = {}
    for neighbour in g.get_neighbours(current_node):
        wrong_part[neighbour] = tree_sum(neighbour)

    c = Counter(list(wrong_part.values()))

    previous_node = current_node
    current_node = None

    for neighbour in wrong_part:
        if c[wrong_part[neighbour]] == 1:
            current_node = neighbour
            break

    if current_node is not None:
        for neighbour in wrong_part:
            if c[wrong_part[neighbour]] != 1:
                balancer = wrong_part[neighbour] - wrong_part[current_node]
                break

    if current_node is None:
        # if this node is balanced, then we still have balancer set from the parent node
        print('Part 2:', previous_node.data + balancer)
        break