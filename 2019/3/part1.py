a = open("input","r").read().strip().split("\n")
a[0] = a[0].split(",")
a[1] = a[1].split(",")
b = [set(),set()]
d = set()
for x in range(0, len(a)):
    cx = 0
    cy = 0
    for y in a[x]:
        for z in range(0, int(y[1:])):
            if y[:1] == "R":
                b[x].add(f"{cx+z},{cy}")
            elif y[:1] == "U":
                b[x].add(f"{cx},{cy+z}")
            elif y[:1] == "L":
                b[x].add(f"{cx-z},{cy}")
            elif y[:1] == "D":
                b[x].add(f"{cx},{cy-z}")
        if y[:1] == "R":
            cx += int(y[1:])
        elif y[:1] == "U":
            cy += int(y[1:])
        elif y[:1] == "L":
            cx -= int(y[1:])
        elif y[:1] == "D":
            cy -= int(y[1:])
c = b[0].intersection(b[1])
for x in c:
    if x != "0,0":
        x = x.split(",")
        if int(x[0]) < 0:
            x[0] = int(x[0]) * -1
        if int(x[1]) < 0:
            x[1] = int(x[1]) * -1
        d.add(int(x[0]) + int(x[1]))
print(min(d))
