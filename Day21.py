from utils import load_input
import numpy as np

rules = load_input('puzzle_inputs/Day21.txt')

transformation_rules = {}


def rule_to_list(s):
    return [1 if x == '#' else 0 for x in s]


for rule in rules:
    s, t = rule.split(' => ')

    if len(s) == 5:
        u, v = s.strip().split('/')
        a = np.array([rule_to_list(u), rule_to_list(v)])

        fv = set()
        frm = [a,np.flip(a,axis=0),np.flip(a,axis=1),np.rot90(a),np.rot90(np.rot90(a)),np.rot90(np.rot90(np.rot90(a)))]

        w, x, y = t.strip().split('/')
        B = np.array([rule_to_list(w), rule_to_list(x), rule_to_list(y)])

        for A in frm:
            sig = tuple(A.flatten())
            if sig in fv:
                continue
            transformation_rules[sig] = B
            fv.add(sig)
    elif len(s) == 11:
        u,v,p = s.strip().split('/')
        a = np.array([rule_to_list(u),rule_to_list(v),rule_to_list(p)])

        fv =  set()

        frm = [a,np.rot90(a),np.rot90(np.rot90(a)),np.rot90(np.rot90(np.rot90(a)))]

        w, x, y, z = t.strip().split('/')
        B = np.array([rule_to_list(w),rule_to_list(x),rule_to_list(y),rule_to_list(z)])

        for A in frm:
            for AA in [A,np.flip(A,axis=0),np.flip(A,axis=1)]:
                sig = tuple(AA.flatten())
                if sig in fv:
                    continue
                transformation_rules[sig] = B
                fv.add(sig)

image = [[0,1,0],
         [0,0,1],
         [1,1,1]]

iter = 0

while iter < 18:
    size = len(image)

    if size % 2 == 0:
        blocks = size // 2
        v = 2
    elif size % 3 == 0:
        blocks = size // 3
        v = 3

    m = []
    for k in range(blocks):
        row = []
        for j in range(blocks):
            block = (np.array(image))[v*k:v*k+v,v*j:v*j+v]
            sig = tuple(block.flatten())

            # find the replacement
            row.append(transformation_rules[sig])
        m.append(np.hstack(row))

    image = np.vstack(m)
    print(iter, sum(image.flatten()))
    iter += 1

print(sum(image.flatten()))

