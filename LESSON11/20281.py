from math import ceil

bit_per_char = 1

while True:
    bytes_per_number = ceil((317 * bit_per_char) / 8)
    total_bytes = bytes_per_number * 487321
    if total_bytes > 130 * 2 ** 20:
        break
    bit_per_char += 1

print(bit_per_char)

print(2 ** (bit_per_char - 1) + 1)
