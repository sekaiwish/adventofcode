a = [*map(int,open("input","r").readlines())]
i = 0
for j in a:
    for k in a[i:]:
        if j + k == 2020:
            print(j * k); exit()
