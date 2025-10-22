from math import log2, ceil

bit = ceil(log2(10 + 52 + 972))
min_length = 1
while True:
    bytes_per_number = ceil((min_length * bit) / 8)
    total_bytes = bytes_per_number * 2048
    if total_bytes > 172 * 1024:
        break
    min_length += 1

print(min_length)

