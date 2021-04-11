with open('input', 'r') as f:
    data = [list(l.strip()) for l in f.readlines()]
c2 = 0; c3 = 0
for line in data:
    countdict = {i:line.count(i) for i in line}
    if 2 in countdict.values():
        c2 += 1
    if 3 in countdict.values():
        c3 += 1
print(c2 * c3)