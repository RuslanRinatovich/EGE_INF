from itertools import product

alphabet = sorted('СТРОКА')

last_number = None
for i, word in enumerate(product(alphabet, repeat=5), start=1):
    if word[0] not in 'АСТ' and word.count('О') == 2 and i % 2 == 0:
        last_number = i  # запоминаем последнее подходящее

print(last_number)
