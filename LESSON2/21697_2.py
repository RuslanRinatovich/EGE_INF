from itertools import product
print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    f = not (x <= y) or (z == w) or z
    if not f:
        print(x, y, z, w)