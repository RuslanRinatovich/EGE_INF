from math import ceil

max_bit = 1
for bit in range(1, 100):
    x = ceil((119 * bit) / 8) * 125300
    if x > 23 * 2 ** 20:
        max_bit = bit
        break

print(2 ** (max_bit - 1) + 1)
