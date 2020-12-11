with open('input', 'r') as fp:
    data = fp.read().strip().split('\n\n')
i = 0; sum = 0
for group in data:
    j = 0
    data[i] = data[i].split('\n')
    for person in data[i]:
        answers = set()
        for answer in person:
            answers.add(answer)
        data[i][j] = answers
        j += 1
    sum += len(data[i][0].intersection(*data[i]))
    i += 1
print(sum)
