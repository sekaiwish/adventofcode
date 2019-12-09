a = [*map(int,open("input","r").read().split(","))]
x = 0

def get_position(x):
    return a[x]
def assign(x, dest):
    a[dest] = x
def calc_params(params, modes):
    modes = modes[::-1]
    for i in range(0, len(modes)):
        if int(modes[i]) == 0:
            params[i] = get_position(params[i])
    return params

while True:
    b = str(a[x]).zfill(5)
    op = int(b[3:])
    if op == 1:
        c = [a[x+1], a[x+2], a[x+3]]
        c = calc_params(c, b[:3])
        assign(c[0] + c[1], a[x+3])
        x += 4
        continue
    elif op == 2:
        c = [a[x+1], a[x+2], a[x+3]]
        c = calc_params(c, b[:3])
        assign(c[0] * c[1], a[x+3])
        x += 4
        continue
    elif op == 3:
        val = int(input("Value: "))
        assign(val, a[x+1])
        x += 2
        continue
    elif op == 4:
        print(f"{a[a[x+1]]}")
        x += 2
        continue
    elif op == 5:
        c = [a[x+1], a[x+2]]
        c = calc_params(c, b[1:3])
        if c[0] != 0:
            x = c[1]
        else:
            x += 3
        continue
    elif op == 6:
        c = [a[x+1], a[x+2]]
        c = calc_params(c, b[1:3])
        if c[0] == 0:
            x = c[1]
        else:
            x += 3
        continue
    elif op == 7:
        c = [a[x+1], a[x+2], a[x+3]]
        c = calc_params(c, b[:3])
        if c[0] < c[1]:
            assign(1, a[x+3])
        else:
            assign(0, a[x+3])
        x += 4
        continue
    elif op == 8:
        c = [a[x+1], a[x+2], a[x+3]]
        c = calc_params(c, b[:3])
        if c[0] == c[1]:
            assign(1, a[x+3])
        else:
            assign(0, a[x+3])
        x += 4
        continue
    elif op == 99:
        break
    print(f"Unhandled opcode: {op}")
    break
