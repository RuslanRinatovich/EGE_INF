from itertools import product
from string import printable
import time

# начальное время
start_time = time.time()

alphabet = printable[:13]

count = 0
for value in product(alphabet, repeat=7):
    number = ''.join(value)
    is_different = len(set(number)) == 7
    for c in '13579':
        number = number.replace(c, '*')
    if number[0] != '0' and is_different and '*b' not in number and 'b*' not in number:
        count += 1

print(count)

# конечное время
end_time = time.time()

# разница между конечным и начальным временем
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
