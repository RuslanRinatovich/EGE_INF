from itertools import product
from string import printable

alphabet = printable[:12]
count = 0
for word in product(alphabet[1:], alphabet, alphabet, alphabet, alphabet):
    number = ''.join(word)
    for c in '13579b':
        number = number.replace(c, '*')
    k = 0
    for i in range(len(number) - 1):
        if number[i] + number[i + 1] == '**':
            k += 1
    if k <= 2:
        count += 1

print(count)
