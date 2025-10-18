def convert_to_3(number):
    s = ''
    while number:
        s = str(number % 3) + s
        number //= 3

    return s


for n in range(200, 0, -1):
    x = convert_to_3(n)
    if n % 3 == 0:
        x = '1' + x + '02'
    else:
        x = x + convert_to_3(n % 3 * 4)
    r = int(x, 3)
    if r < 100:
        print(n)
        break
