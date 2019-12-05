from math import floor
a = [*map(int,open("input","r").readlines())]
b = 0
for i in a:
    while True:
        c = floor(i/3)-2
        if c < 0:
            break
        b += c
        i = c
print(b)
