with open('input', 'r') as fp:
    data = [line.rstrip() for line in fp]
coordinate = [0, 0]; hits = 0
while True:
    coordinate[0] += 3; coordinate[1] += 1
    if coordinate[0] >= 31:
        coordinate[0] = coordinate[0] % 31
    try:
        if data[coordinate[1]][coordinate[0]] == '#':
            hits += 1
    except IndexError:
        break
print(hits)
