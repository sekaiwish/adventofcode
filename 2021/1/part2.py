with open('input', 'r') as fp:
    data = [int(line.rstrip()) for line in fp]
increased = 0
i = 0
for _ in data[:-2]:
    data[i] += data[i+1] + data[i+2]
    i += 1
previous = data[0]
for line in data[:-2]:
    if line > previous:
        increased += 1
    previous = line
print(increased)