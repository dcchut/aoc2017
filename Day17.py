state = [0]
step_size = 369
current_position = 0
current_value = 1

while current_value <= 2017:
    current_position = (current_position + step_size) % len(state)
    state.insert(current_position+1,current_value)
    current_value += 1
    current_position += 1

print('Part 1:', state[(current_position+1) % len(state)])

# For part 2, instead of tracking the entire state, we just keep track of where 0 is,
# and what the number after 0 is
state = 1
step_size = 369
current_position = 0
current_zero = 0
current_value = 1
current_after = None

while current_value <= 50000000:
    current_position = (current_position + step_size) % state
    state += 1

    if current_position == current_zero:
        current_after = current_value

    # if we're inserting at the end of the list, then move our zero position counter to the right
    if (current_position + 1) % state == current_zero:
        current_zero += 1
    # if we're inserting to the left of the current 0, move our zero position counter to the right
    elif current_position + 1 <= current_zero:
        current_zero += 1

    current_value += 1
    current_position += 1

print('Part 2:', current_after)