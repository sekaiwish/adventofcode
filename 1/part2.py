frequencies = open("input", "r").read().strip().split("\n")
total_frequency = 0
previous_freqs = []
dupe_found = False
while dupe_found is False:
    for frequency in frequencies:
        if frequency.startswith("+"):
            total_frequency += int(frequency[1:])
        else:
            total_frequency -= int(frequency[1:])
        if total_frequency in previous_freqs:
            print("Found duplicate", total_frequency)
            dupe_found = True
            break
        previous_freqs.append(total_frequency)
