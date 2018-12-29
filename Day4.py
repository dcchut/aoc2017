from utils import load_input

puzzle_input = load_input('puzzle_inputs/Day4.txt')

def valid_passphrase(line):
    seen_words = set()
    for word in line.split():
        if word in seen_words:
            return False
        seen_words.add(word)
    return True

def valid_passphrase_v2(line):
    seen_words = set()
    for word in line.split():
        word = ''.join(sorted(word, key=ord))
        if word in seen_words:
            return False
        seen_words.add(word)
    return True

c1 = 0
c2 = 0
for line in puzzle_input:
    if valid_passphrase(line):
        c1 += 1
    if valid_passphrase_v2(line):
        c2 += 1

print('Part 1:', c1)
print('Part 2:', c2)