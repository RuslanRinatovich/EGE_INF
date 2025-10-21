from itertools import product

count = 0
for value in product('0123456', repeat=5):
    is_norm = True
    for i in range(4):
        if value[i] == value[i + 1]:
            is_norm = False
            break

    if value[0] != '0' and value.count('6') == 1 and is_norm:
        count += 1

print(count)
