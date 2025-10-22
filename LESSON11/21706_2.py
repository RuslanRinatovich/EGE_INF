from math import ceil

bit_for_symbol = 0
for bit in range(1, 100):
    x = ceil((bit * 119) / 8)
    if bit_for_symbol == 0 and x * 125300 > 23 * 2 ** 20: # 2
        bit_for_symbol = bit
        print(bit)


print(2 ** bit_for_symbol, 2 ** (bit_for_symbol - 1) + 1)
