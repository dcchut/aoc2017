# simple functions for working with points in cartesian space
def adjacent(p):
    return [(p[0]-1,p[1]-1),(p[0]-1,p[1]),(p[0]-1,p[1]+1),(p[0],p[1]-1),(p[0],p[1]+1),(p[0]+1,p[1]-1),(p[0]+1,p[1]),(p[0]+1,p[1]+1)]


def left(p):
    return (p[0]-1,p[1])


def right(p):
    return (p[0]+1,p[1])


def up(p):
    return (p[0],p[1]-1)


def down(p):
    return (p[0],p[1]+1)