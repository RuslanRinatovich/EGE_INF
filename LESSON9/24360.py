data_sums = []
for line in open('data.txt'):
    data = [int(x) for x in line.split()]
    f1 = (min(data) ** 2) in data
    counts = [data.count(c) for c in set(data)]
    total_pairs = sum(count // 2 for count in counts)
    f2 = total_pairs >= 3
    if f1 != f2:
        data_sums.append(sum(data))

print(min(data_sums))
