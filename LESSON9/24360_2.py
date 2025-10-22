data_sums = []
for line in open('data.txt'):
    data = [int(x) for x in line.split()]
    f1 = (min(data) ** 2) in data
    counts = sorted([data.count(c) for c in set(data)])
    f2 = counts in [[1, 1, 2, 2, 2], [2, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2], [2, 2, 4], [1, 1, 2, 4]]
    if f1 != f2:
        print(data, counts, f1, f2)
        data_sums.append(sum(data))

print(min(data_sums))
