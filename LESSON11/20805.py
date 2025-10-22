from math import ceil

bit_per_char = 1
while True:
    bytes_per_number = ceil((248 * bit_per_char) / 8)
    total_bytes = bytes_per_number * 75600
    if total_bytes > 16 * 2 ** 20:
        break
    bit_per_char += 1

print(2 ** (bit_per_char - 1) + 1)
