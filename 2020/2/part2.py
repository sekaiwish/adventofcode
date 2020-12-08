data = []
with open('input', 'r') as fp:
    for line in fp:
        entry = line.replace('-', ' ').replace(': ', ' ').split()
        data.append(entry)
valid = 0
for i in data:
    if bool(i[3][int(i[0])-1] == i[2]) ^ bool(i[3][int(i[1])-1] == i[2]):
        valid += 1
print(valid)
