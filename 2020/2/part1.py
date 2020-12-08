data = []
with open('input', 'r') as fp:
    for line in fp:
        entry = line.replace('-', ' ').replace(': ', ' ').split()
        data.append(entry)
valid = 0
for i in data:
    if i[3].count(i[2]) in range(int(i[0]), int(i[1]) + 1):
        valid += 1
print(valid)
