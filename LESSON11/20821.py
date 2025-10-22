from math import ceil, log2

bit_for_char = ceil(log2(26 + 10))
bytes_per_number = ceil(9 * bit_for_char / 8)
info_for_user = 40 + bytes_per_number
k = 30 * 2 ** 10 / info_for_user
print(int(k))

print(653 * info_for_user <= 30 * 2 ** 10)
print(654 * info_for_user <= 30 * 2 ** 10)

