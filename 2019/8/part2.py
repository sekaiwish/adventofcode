a = open("input","r").read().strip()
l = 25 * 6
d = []
while True:
    p = a[:l]
    if not p:
        break
    a = a[l:]
    d.append(p)
chars = 0
for y in range(0, len(d[0])):
    depth = 0
    while True:
        if d[depth][y] != '2':
            print(" " if d[depth][y] == '0' else "#", end = "")
            break
        else:
            depth += 1
    chars += 1
    if chars > 24:
        chars = 0
        print("")
