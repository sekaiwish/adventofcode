from math import ceil
a = [*map(int,open("input","r").read().strip())]
b = [0, 1, 0, -1]
e = []
for _ in range(100):
    e.clear()
    for j in range(1, len(a) + 1):
        c = [b[k//j] for k in range(len(b)*j)]
        c = (c * (ceil(len(a) / len(c))))[1:]
        d = 0
        for k in range(len(a)):
            if c[k] == 0:
                continue
            d += int(a[k]) * c[k]
        e.append(str(d)[-1])
    a = [*map(int,e)]
print("".join(map(str, a[:8])))
