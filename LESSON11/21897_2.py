from math import ceil

max_bit = 0
for bit in range(1, 100):
    x = ceil((246 * bit) / 8)
    if x * 703569 <= 77 * 2 ** 20:
        max_bit = bit
        print(bit)

print(2 ** max_bit)