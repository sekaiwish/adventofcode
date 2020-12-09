with open('input', 'r') as fp:
    a = fp.read().split('\n\n')
def check_fields(i):
    for field in a[i]:
        if field.split(':')[0] == 'cid':
            return False
    return True
i = 0; valid = 0
for line in a:
    a[i] = a[i].replace('\n', ' ').strip().split()
    if len(a[i]) == 8:
        valid += 1
    elif len(a[i]) == 7:
        if check_fields(i):
            valid += 1
    i += 1
print(valid)
