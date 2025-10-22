from math import ceil

max_bit = None
for bit in range(100, 0, -1):
    x = ceil((257 * bit) / 8)
    if x * 295740 <= 33 * 2 ** 20:
        max_bit = bit
        break
print(2 ** max_bit)
