from utils import load_input, get_numbers
from collections import defaultdict

puzzle_input = load_input('puzzle_inputs/Day8.txt')

r = defaultdict(int)
code = ""
current_max = 0

for line in puzzle_input:
    delta, condition = get_numbers(line)
    operation = line.split()[1]
    variable = line.split()[0]
    condition_variable = line.split(' if ')[1].split(' ')[0]
    conditional = line.split(f'if {condition_variable} ')[1].split()[0]

    # we translate the code to pure python
    code = f"if r['{condition_variable}'] {conditional} {condition}:\n"

    if operation == 'inc':
        code += f"\tr['{variable}'] += {delta}\n"
    else:
        code += f"\tr['{variable}'] -= {delta}\n"

    # evalate, then check what the maximum value of any register is
    exec(code)

    m = r[max(r, key=r.get)]
    if m > current_max:
        current_max = m

print('Part 1:',r[max(r,key=r.get)])
print('Part 2:',current_max)