i = input("Gebe Zahlen ein: ")
l = i.split(" ")
sorted = list()
for n in l:
    if sorted == []: # means sorted in empty
        sorted.append(n)
    else:
        index = 0
        while index < len(sorted) and sorted[index] < n:
            index += 1
        final_index = index
        sorted_cache = sorted
        for index in range(index - 1, len(sorted)):
            if index == len(sorted):
                sorted.append(n)
            else:
                sorted[index + 1] = sorted_cache[index]
            sorted[final_index] = n
print(sorted)
