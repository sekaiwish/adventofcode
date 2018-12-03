frequency = 0
reachedFrequencies = []
duplicateFound = False
with open("input", "r") as input:
    for line in input:
        if line[0] == "+":
            frequency += int(line[1:-1])
        else:
            frequency -= int(line[1:-1])
        if duplicateFound == False:
            if frequency in reachedFrequencies:
                duplicateFound = True
            else:
                reachedFrequencies.append(frequency)
    print("No duplicate found")
