def load():
    a = [*map(int, open("input", "r").read().split(","))]
    return a
a = load()
for i in range(1, 100):
    for j in range(1, 100):
        x = 0
        a[1] = i
        a[2] = j
        while True:
            if a[x] == 1:
                a[a[x+3]] = a[a[x+1]] + a[a[x+2]]
                x += 4
                continue
            elif a[x] == 2:
                a[a[x+3]] = a[a[x+1]] * a[a[x+2]]
                x += 4
                continue
            elif a[x] == 99:
                if a[0] == 19690720:
                    print(100 * i + j)
                a = load()
                break
