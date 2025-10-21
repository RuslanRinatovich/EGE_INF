from itertools import product

count = 0

for word in product('ДГИАШЭ', repeat=5):
    if word[0] not in 'ИАЭ' and word[-1] not in 'ДГШ':
        count += 1

print(count)
