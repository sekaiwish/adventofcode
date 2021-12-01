with open('input', 'r') as fp:
    data = [line.rstrip() for line in fp]
executed = set()
accumulator = 0
instruction = 0
while True:
    if instruction in executed:
        print(accumulator); exit()
    executed.add(instruction)
    op = data[instruction][:3]
    value = int(data[instruction][5:]) if (data[instruction][4] == '+') else (int(data[instruction][5:]) * -1)
    if op == 'nop':
        instruction += 1; continue
    if op == 'acc':
        instruction += 1; accumulator += value; continue
    if op == 'jmp':
        instruction += value; continue