a = open("input","r").read().strip()
l = 25 * 6
i = []
while True:
    p = a[:l]
    if not p:
        break
    a = a[l:]
    i.append(p)
lowest = len(i[0])
for x in range(0, len(i)):
    count = 0
    for y in range(0, len(i[x])):
        if i[x][y] == '0':
            count += 1
    if count < lowest:
        lowest = count
        layer = x
ones = 0
twos = 0
for x in range(0, len(i[layer])):
    if i[layer][x] == '1':
        ones += 1
    elif i[layer][x] == '2':
        twos += 1
print(ones * twos)
