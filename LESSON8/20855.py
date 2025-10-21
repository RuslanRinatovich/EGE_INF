from itertools import product
from string import printable

alphabet = printable[:13]
count = 0
for i, word in enumerate(product(alphabet[1:], alphabet, alphabet), start=0):
    number = ''.join(word)
    for c in '13579b':
        number = number.replace(c, '*')
    if '**' not in number and i % 10 == 7:
        count += 1

print(count)
