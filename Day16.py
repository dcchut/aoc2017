from utils import load_input, get_numbers, memoize


def letter(index):
    return chr(index+97)

def perform_dance(state):
    new_state = state.copy()
    for move in dance:
        if move[0] == 'x' or move[0] == 'p':
            if move[0] == 'p':
                p = new_state.index(move[1])
                q = new_state.index(move[2])
            else:
                p = move[1]
                q = move[2]
            z = new_state[p]
            new_state[p] = new_state[q]
            new_state[q] = z
        elif move[0] == 's':
            x = move[1]
            new_state = new_state[-x:] + new_state[:-x]

    return new_state


puzzle_input = load_input("puzzle_inputs/Day16.txt")[0].split(",")

dance = []

for move in puzzle_input:
    move_type = move[0]

    if move_type == 's':
        spin_by = get_numbers(move)[0]
        dance.append(('s',spin_by))
    elif move_type == 'x':
        v1, v2 = get_numbers(move)
        dance.append(('x', v1, v2))
    else:
        z = move[1:].replace('/','')
        dance.append(('p',z[0],z[1]))

state = [letter(q) for q in range(16)]
state = perform_dance(state)
print('Part 1:', ''.join(state))

# For part 2, we do some simple repetition detection
state = [letter(q) for q in range(16)]
visited = {}
k = 0
while k < 1000000000:
    # if the dance has ever been in this state before,
    # we can "skip forward through time" a bit
    sig = tuple(state)
    if sig in visited:
        # last index
        k_loop_size = k - visited[sig]
        while k + k_loop_size < 1000000000:
            k += k_loop_size

    state = perform_dance(state)
    visited[sig] = k
    k += 1

print('Part 2:', ''.join(state))