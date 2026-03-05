lines = sorted(eval(open('names.txt').read()))

total_score = 0
for index, line in enumerate(lines, start=1):
    total_score += index * sum(ord(c) - 64 for c in line)

# Alternative with alphabet
total_score = 0
for index, line in enumerate(lines, start=1):
    total_score += index * sum(alphabet.index(c)+1 for c in line)