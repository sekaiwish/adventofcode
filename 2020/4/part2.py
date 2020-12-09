# Does not generate correct answer

import re
with open('input', 'r') as fp:
    a = fp.read().split('\n\n')
def check_fields(i):
    if len(a[i]) == 7:
        for field in a[i]:
            if field.split(':')[0] == 'cid':
                return False
    for field in a[i]:
        value = field.split(':')
        if value[0] == 'byr':
            match = re.search(r'(19[2-9]\d|200[012])', value[1])
            if not match:
                return False
        if value[0] == 'iyr':
            match = re.search(r'(201\d|2020)', value[1])
            if not match:
                return False
        if value[0] == 'eyr':
            match = re.search(r'(202\d|2030)', value[1])
            if not match:
                return False
        if value[0] == 'hgt':
            match = re.search(r'(1[5-8]\d|19[0-3])(?=cm)|(59|6\d|7[0-6])(?=in)', value[1])
            if not match:
                return False
        if value[0] == 'hcl':
            match = re.search(r'#[0-9a-f]{6}', value[1])
            if not match:
                return False
        if value[0] == 'ecl':
            match = re.search(r'amb|blu|brn|gry|grn|hzl|oth', value[1])
            if not match:
                return False
        if value[0] == 'pid':
            match = re.search(r'^\d{9}$', value[1])
            if not match:
                return False
    return True
i = 0; valid = 0
for line in a:
    a[i] = a[i].replace('\n', ' ').strip().split()
    if len(a[i]) >= 7:
        if check_fields(i):
            valid += 1
    i += 1
print(valid)
