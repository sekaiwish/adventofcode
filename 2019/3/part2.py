a = open("input","r").read().strip().split("\n")
a[0] = a[0].split(",")
a[1] = a[1].split(",")
b = [{},{}]
c = [set(),set()]
d = []
for x in range(0, len(a)):
    cx = 0
    cy = 0
    dis = 0
    for y in a[x]:
        for z in range(0, int(y[1:])):
            if y[:1] == "R":
                b[x][dis] = f"{cx+z},{cy}"
            elif y[:1] == "U":
                b[x][dis] = f"{cx},{cy+z}"
            elif y[:1] == "L":
                b[x][dis] = f"{cx-z},{cy}"
            elif y[:1] == "D":
                b[x][dis] = f"{cx},{cy-z}"
            dis += 1
        if y[:1] == "R":
            cx += int(y[1:])
        elif y[:1] == "U":
            cy += int(y[1:])
        elif y[:1] == "L":
            cx -= int(y[1:])
        elif y[:1] == "D":
            cy -= int(y[1:])
c = set(b[0].values()).intersection(set(b[1].values()))
for x in c:
    d.append(list(b[0].keys())[list(b[0].values()).index(x)] + list(b[1].keys())[list(b[1].values()).index(x)])
print(min(i for i in d if i > 0))
