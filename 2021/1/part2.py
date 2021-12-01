with open('input', 'r') as fp:
    data = [int(line.rstrip()) for line in fp]
increased = 0
i = 0
previous = data[0] + data[1] + data[2]
for _ in data[:-2]:
    data[i] += data[i+1] + data[i+2]
    if data[i] > previous:
        increased += 1
    previous = data[i]
    i += 1
print(increased)