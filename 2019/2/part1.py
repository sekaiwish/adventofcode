a = [*map(int,open("input","r").read().split(","))]
a[1] = 12
a[2] = 2
x = 0
while True:
    if a[x] == 1:
        a[a[x+3]] = a[a[x+1]] + a[a[x+2]]
        x += 4
    elif a[x] == 2:
        a[a[x+3]] = a[a[x+1]] * a[a[x+2]]
        x += 4
    elif a[x] == 99:
        break
print(a[0])
