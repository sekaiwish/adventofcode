frequencies = open("input", "r").read().strip().split("\n")
total_frequency = 0
previous_freqs = {0}
while True:
    for frequency in frequencies:
        total_frequency += int(frequency)
        if total_frequency in previous_freqs:
            print(f"Duplicate frequency: {total_frequency}")
            exit()
        previous_freqs.add(total_frequency)
