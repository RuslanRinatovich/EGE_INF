from math import log2, ceil

bit = ceil(log2(10 + 26 + 32724))
serial_number = ceil((223 * bit) / 8)
x = 17 * 2 ** 30 / serial_number
print(int(x))

