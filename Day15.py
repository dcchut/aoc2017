from utils import memoize

def a_step(q):
    return (q * 16807) % 2147483647

def b_step(q):
    return (q * 48271) % 2147483647

@memoize
def a_step_2(q):
    z = (q * 16807) % 2147483647
    while z % 4 != 0:
        z = (z * 16807) % 2147483647
    return z

@memoize
def b_step_2(q):
    z = (q * 48271) % 2147483647
    while z % 8 != 0:
        z = (z * 48271) % 2147483647
    return z

a_value = 512
b_value = 191

matches = 0
for k in range(40000000):
    break
    a_value = a_step(a_value)
    b_value = b_step(b_value)
    if "{0:032b}".format(a_value)[16:] == "{0:032b}".format(b_value)[16:]:
        matches += 1

print('Part 1:', matches)

matches = 0
for k in range(5000000):
    a_value = a_step_2(a_value)
    b_value = b_step_2(b_value)
    if "{0:032b}".format(a_value)[16:] == "{0:032b}".format(b_value)[16:]:
        matches += 1

print('Part 2:', matches)