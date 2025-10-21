from itertools import product

alphabet = '012345678'
count = 0
for number in product(alphabet, repeat=5):
    n = ''.join(number)
    for c in '1357':
        n = n.replace(c, '*')
    if n[0] != '0' and n.count('0') == 1 and '*0' not in n and '0*' not in n:
        count += 1

print(count)
