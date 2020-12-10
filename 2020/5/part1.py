with open('input', 'r') as fp:
    data = [line.rstrip() for line in fp]
def calc_bits(raw):
    value = 1; result = 0
    for bit in raw:
        if bit == 'B' or bit == 'R':
            result += value
        value *= 2
    return result
ids = []
for seat in data:
    row = calc_bits(seat[:7][::-1])
    column = calc_bits(seat[7:][::-1])
    ids.append(row * 8 + column)
print(max(ids))
