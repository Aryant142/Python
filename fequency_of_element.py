elements = ['a', 'b', 'c', 'a', 'd', 'b', 'c', 'c', 'e', 'f', 'g', 'a', 'b', 'c']

frequency = {}

for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print(frequency)