a = open("input","r").read().strip().split("\n")
a[0] = a[0].split(",")
a[1] = a[1].split(",")
b = []
c = []
d = []
e = []
cx = 0
cy = 0
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
for x in b:
    if x in c:
        d.append(x)
for x in d:
    x = x.split(",")
    if int(x[0]) < 0:
        x[0] = int(x[0]) * -1
    if int(x[1]) < 0:
        x[1] = int(x[1]) * -1
    e.append(int(x[0]) + int(x[1]))
lowest = e[1]
for x in e[1:]:
    if x < lowest:
        lowest = x
print(lowest)
