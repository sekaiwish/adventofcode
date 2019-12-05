a = [*map(int,open("input","r").read().strip().split("-"))]
b = min(a)
c = 0
while b < max(a):
    d = 0
    if str(b)[0] == str(b)[1] and str(b)[1] != str(b)[2]:
        d = 1
    elif str(b)[1] == str(b)[2] and str(b)[2] != str(b)[3] and str(b)[0] != str(b)[1]:
        d = 1
    elif str(b)[2] == str(b)[3] and str(b)[3] != str(b)[4] and str(b)[1] != str(b)[2]:
        d = 1
    elif str(b)[3] == str(b)[4] and str(b)[4] != str(b)[5] and str(b)[2] != str(b)[3]:
        d = 1
    elif str(b)[4] == str(b)[5] and str(b)[3] != str(b)[4]:
        d = 1
    if d == 1:
        if not int(str(b)[0]) > int(str(b)[1])\
        and not int(str(b)[1]) > int(str(b)[2])\
        and not int(str(b)[2]) > int(str(b)[3])\
        and not int(str(b)[3]) > int(str(b)[4])\
        and not int(str(b)[4]) > int(str(b)[5]):
            c += 1
    b += 1
print(c)
