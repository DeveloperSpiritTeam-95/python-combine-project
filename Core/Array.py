array = [10, 30, 25, 10, 40, 60, 10, 60, 10]
element_counts = {}

for element in array:
    element_counts[element] = element_counts.get(element, 0) + 1
    if element_counts[element] > 1:
        print(element)
