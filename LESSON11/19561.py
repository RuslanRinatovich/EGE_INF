from math import log2, ceil

bit_per_char = ceil(log2(10 + 26 + 496))
serial_number_len = 1
while True:
    bytes_per_serial_number = ceil((serial_number_len * bit_per_char) / 8)
    total_bytes = bytes_per_serial_number *725
    if total_bytes > 353 * 2 ** 10:
        break
    serial_number_len += 1

print(serial_number_len)


