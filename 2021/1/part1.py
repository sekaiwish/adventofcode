with open('input', 'r') as fp:
    data = [int(line.rstrip()) for line in fp]
previous = data[0]
increased = 0
for line in data:
    if line > previous:
        increased += 1
    previous = line
print(increased)