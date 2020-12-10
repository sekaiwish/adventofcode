with open('input', 'r') as fp:
    data = fp.read().split('\n\n')
i = 0; sum = 0
for group in data:
    data[i] = data[i].replace('\n', '')
    answers = set()
    for answer in data[i]:
        answers.add(answer)
    sum += len(answers)
    i += 1
print(sum)
