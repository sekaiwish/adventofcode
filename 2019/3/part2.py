a = open("input","r").read().strip().split("\n")
a[0] = a[0].split(",")
a[1] = a[1].split(",")
b, c, d = [], [], []
cx, cy = 0, 0
for x in a[0]:
    for y in range(0, int(x[1:])):
        if x[:1] == "R":
            b.append(f"{cx+y},{cy}")
        elif x[:1] == "U":
            b.append(f"{cx},{cy+y}")
        elif x[:1] == "L":
            b.append(f"{cx-y},{cy}")
        elif x[:1] == "D":
            b.append(f"{cx},{cy-y}")
    if x[:1] == "R":
        cx += int(x[1:])
    elif x[:1] == "U":
        cy += int(x[1:])
    elif x[:1] == "L":
        cx -= int(x[1:])
    elif x[:1] == "D":
        cy -= int(x[1:])
cx = 0
cy = 0
for x in a[1]:
    for y in range(0, int(x[1:])):
        if x[:1] == "R":
            c.append(f"{cx+y},{cy}")
        elif x[:1] == "U":
            c.append(f"{cx},{cy+y}")
        elif x[:1] == "L":
            c.append(f"{cx-y},{cy}")
        elif x[:1] == "D":
            c.append(f"{cx},{cy-y}")
    if x[:1] == "R":
        cx += int(x[1:])
    elif x[:1] == "U":
        cy += int(x[1:])
    elif x[:1] == "L":
        cx -= int(x[1:])
    elif x[:1] == "D":
        cy -= int(x[1:])
for x in range(0, len(b)):
    if b[x] in c:
        d.append(b.index(b[x]) + c.index(b[x]))
print(min(d[1:]))
