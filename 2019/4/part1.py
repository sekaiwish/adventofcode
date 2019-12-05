a = [*map(int,open("input","r").read().strip().split("-"))]
b = min(a)
c = 0
while b < max(a):
    if str(b)[0] == str(b)[1]\
    or str(b)[1] == str(b)[2]\
    or str(b)[2] == str(b)[3]\
    or str(b)[3] == str(b)[4]\
    or str(b)[4] == str(b)[5]:
        if not int(str(b)[0]) > int(str(b)[1])\
        and not int(str(b)[1]) > int(str(b)[2])\
        and not int(str(b)[2]) > int(str(b)[3])\
        and not int(str(b)[3]) > int(str(b)[4])\
        and not int(str(b)[4]) > int(str(b)[5]):
            c += 1
    b += 1
print(c)
