from itertools import product

i = 0
for value in product(sorted('КОТЕНА'), repeat=7):
    i += 1
    if sorted('КОТЕНОК') == sorted(value) and i % 2 == 1:
        print(i, value)
