with open('input', 'r') as f:
    data = [l.strip() for l in f.readlines()]

for i in data:
    for j in data:
        if j == i: continue
        delta = 0; k = 0
        for _ in j:
            if i[k] != j[k]: delta += 1
            if delta > 1: break
            k += 1
        if delta == 1:
            k = 0
            for _ in i:
                print(i[k] if i[k] == j[k] else '', end=''); k += 1
            print(''); exit()