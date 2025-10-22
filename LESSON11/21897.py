from math import ceil
max_bit = 1
for bit in range(1, 100):
    x = ceil((257 * bit) / 8) * 295740
    if x <= 33 * 2 ** 20:
        max_bit = bit

print(max_bit, 2 ** max_bit)

