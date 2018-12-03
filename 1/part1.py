frequency = 0
with open("input", "r") as fp:
    for line in fp:
        if line[0] == "+":
            frequency += int(line[1:-1])
        else:
            frequency -= int(line[1:-1])
print(f"Final frequency: {frequency}")
