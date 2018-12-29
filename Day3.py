from cartesian import adjacent, left, right, up, down

puzzle_input = 277678

records = {}
values = {(0,0) : 1}
current_position = (0,0)
current_count = 1
current_state = 0

# xmax, ymin, xmin, ymax
bounds = [0,0,0,0]

while current_count <= puzzle_input:
    if current_state == 0:
        condition = lambda q: q[0] <= bounds[0]
        modifier = right
    elif current_state == 1:
        condition = lambda q: q[1] >= bounds[1]
        modifier = up
    elif current_state == 2:
        condition = lambda q: q[0] >= bounds[2]
        modifier = left
    else:
        condition = lambda q: q[1] <= bounds[3]
        modifier = down
    while condition(current_position):
        current_position = modifier(current_position)
        current_count += 1
        records[current_count] = current_position

        current_value = 0
        for check_position in adjacent(current_position):
            if check_position in values:
                current_value += values[check_position]

        values[current_position] = current_value

    bounds[current_state] = current_position[current_state % 2]
    current_state = (current_state + 1) % 4

print('Part 1:', sum(abs(n) for n in records[puzzle_input]))

for k in values:
    if values[k] > puzzle_input:
        print('Part 2:',values[k])
        break