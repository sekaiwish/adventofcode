a = [*map(int,open("input","r").readlines())]
i = 0
for j in a:
    for k in a:
        for l in a:
            if j + k + l == 2020:
                print(j * k * l); exit()
