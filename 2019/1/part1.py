from math import floor
a = [*map(int,open("input","r").readlines())]
b = 0
for i in a:
    b += floor(i/3)-2
print(b)
