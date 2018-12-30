from utils import load_input, get_numbers, manhattan_distance
import numpy as np


def triangular(n):
    return n*(n+1) // 2


v = {}
a = {}
p = {}

for (k,line) in enumerate(load_input('puzzle_inputs/Day20.txt')):
    px,py,pz,vx,vy,vz,ax,ay,az = get_numbers(line)
    v[k] = (vx,vy,vz)
    a[k] = (ax,ay,az)
    p[k] = (px,py,pz)

v = np.array(list(v.values()), dtype='int64')
a = np.array(list(a.values()), dtype='int64')
p = np.array(list(p.values()), dtype='int64')

# part 1
# a closed for for the position after t steps is
# p_i(t) = p_i(0) + t * v_i + triangular(t) * a_i
large_number = 500000000

d = p+large_number*v + triangular(large_number)*a

print('Part 1:', min(enumerate(d),key=lambda q:manhattan_distance(q[1],(0,0,0)))[0])

# part 2
# just brute force it
collided = set()


while True:
    v += a
    p += v

    update_collided = set()
    for (k1,q1) in enumerate(p):
        if k1 in collided:
            continue
        for (k2,q2) in enumerate(p):
            if k1 == k2 or k2 in collided:
                continue
            d = q1 - q2

            if d[0] == 0 and d[1] == 0 and d[2] == 0:
                update_collided.add(k1)
                update_collided.add(k2)

    collided = collided.union(update_collided)
    print(1000-len(collided))