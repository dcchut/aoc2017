import multiprocessing
import re
from collections import defaultdict
from joblib import Parallel, delayed


def load_input(filename):
    # load the input data
    with open(filename, 'r') as fh:
        data = fh.read()

    return data.split('\n')


def get_numbers(string):
    # get all of the numbers appearing in a given string
    return mapint(re.findall(r"(-?\d+)", string))


def mapli(li, fn):
    return [fn(q) for q in li]


def mapint(li):
    return mapli(li, int)


def mapstr(li):
    return mapli(li, str)


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def parallel_map(inputs, fn, unpack=False):
    num_cores = multiprocessing.cpu_count()

    # if the unpack parameter is true, then unpack each input into our function
    if unpack:
        return Parallel(n_jobs=num_cores)(delayed(fn)(*q) for q in inputs)
    else:
        return Parallel(n_jobs=num_cores)(delayed(fn)(q) for q in inputs)


def flatten_list(li):
    return [item for sublist in li for item in sublist]


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# A basic circular doubly linked list implementation
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None

    # insert new_node <after> node
    def insert(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        new_node.next.prev = new_node
        node.next = new_node

    # insert new_node at end
    def append(self, new_node):
        # if the list is empty, then this is our list!
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # otherwise insert after the last thing in our list
            self.insert(self.first.prev, new_node)

    # remove a node from the list
    def remove(self, node):
        # if the list has a single element
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            # update self.first if we removed the first node
            if self.first == node:
                self.first = node.next


def manhattan_distance(p,q):
    return sum(abs(p[0]-p[1]) for p in zip(p,q))


def memoize(func):
    store = {}

    def wrapper_memoize(*args,**kwargs):
        signature = (args,tuple(zip(kwargs, kwargs.values())))
        if signature not in store:
            store[signature] = func(*args,**kwargs)
        return store[signature]
    return wrapper_memoize

def constraint_choose(is_max,li,*keys):
    fn = max if is_max else min
    return fn(li, key=lambda x: tuple(f(x) for f in keys))


def constraint_max(li, *keys):
    return constraint_choose(True, li, *keys)


def constraint_min(li, *keys):
    return constraint_choose(False, li, *keys)


class GraphNode:
    def __init__(self, data):
        self.graph = None
        self.data = data

    def __repr__(self):
        return f"Node(data={str(self.data)})"

class Edge:
    def __init__(self, s, t, weight=1):
        self.s = s
        self.t = t
        self.weight = weight

    def __repr__(self):
        return f"Edge(s={str(self.s.data)},t={str(self.t.data)})"


class Graph:
    nodes = set()
    edges = defaultdict(set)

    def __repr__(self):
        s = 'Graph\nNodes:'
        s += str(self.nodes)
        s += '\nEdges:'
        s += str(self.edges)

        return s

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_node(self, node):
        # add the node to this graph
        node.graph = self
        self.nodes.add(node)

    def add_edge_by_node(self, s, t, weight=1):
        self.add_edge(Edge(s,t,weight))

    def add_edge(self, e):
        self.edges[e.s].add(e)

    def add_edges(self, edges):
        for e in edges:
            self.add_edge(e)

    # get all nodes that can be reached via a single edge from src node
    def get_neighbours(self, src):
        return [edge.t for edge in self.edges[src]]

    # get all edges that start at src node
    def get_edges(self, src):
        return self.edges[src]

    def shortest_path_lengths(self, src):
        # find the lengths of the shortest path along the graph
        # starting at src
        shortest_length = defaultdict(int)
        shortest_length[src] = 0

        queue = set([src])

        while len(queue) > 0:
            current_node = queue.pop()

            for e in self.get_edges(current_node):
                path_length = shortest_length[current_node] + e.weight

                if e.t not in shortest_length or path_length < shortest_length[e.t]:
                    shortest_length[e.t] = path_length
                    queue.add(e.t)

        return shortest_length

    def shortest_paths(self, src):
        # get all of the shortest paths on the graph, starting at src
        shortest_paths = {src: (0, [])}

        queue = [(src,[])]

        while len(queue) > 0:
            current_node, current_path = queue.pop()

            for e in self.get_edges(current_node):
                path_length = shortest_paths[current_node][0] + e.weight

                if e.t not in shortest_paths or path_length < shortest_paths[e.t][0]:
                    new_path = current_path + [e]
                    shortest_paths[e.t] = (path_length, new_path)
                    queue.append([e.t, new_path])

        return shortest_paths