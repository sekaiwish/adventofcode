with open('input', 'r') as fp:
    data = [line.rstrip() for line in fp]
def find_trees(dx, dy):
    coordinate = [0, 0]; hits = 0
    while True:
        coordinate[0] += dx; coordinate[1] += dy
        if coordinate[0] >= 31:
            coordinate[0] = coordinate[0] % 31
        try:
            if data[coordinate[1]][coordinate[0]] == '#':
                hits += 1
        except IndexError:
            return hits
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]; result = 1
for deltas in slopes:
    result = find_trees(deltas[0], deltas[1]) * result
print(result)
