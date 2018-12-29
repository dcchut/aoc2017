from utils import load_input, get_numbers, Graph, GraphNode, memoize


@memoize
def get_or_create_node(n):
    node = GraphNode(n)
    nodes.add(node)
    return node

puzzle_input = load_input('puzzle_inputs/Day12.txt')

nodes = set()
g = Graph()

for line in puzzle_input:
    pg = get_numbers(line)
    src = pg[0]
    targets = pg[1:]

    src_node = get_or_create_node(src)

    for target in targets:
        target_node = get_or_create_node(target)
        g.add_edge_by_node(src_node, target_node)


groups = 0

while True:
    current_parent = nodes.pop()
    network = set([current_parent])
    process = set([current_parent])

    groups += 1
    while len(process) > 0:
        node = process.pop()
        for neighbour in g.get_neighbours(node):
            if neighbour not in network:
                network.add(neighbour)
                process.add(neighbour)
                nodes.remove(neighbour)

    if get_or_create_node(0) in network:
        print('Part 1:', len(network))

    if len(nodes) == 0:
        break

print('Part 2:', groups)






