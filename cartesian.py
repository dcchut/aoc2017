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


def turn_right(direction):
    if direction == up:
        return right
    elif direction == right:
        return down
    elif direction == down:
        return left
    elif direction == left:
        return up


def turn_left(direction):
    if direction == up:
        return left
    if direction == right:
        return up
    if direction == down:
        return right
    if direction == left:
        return down