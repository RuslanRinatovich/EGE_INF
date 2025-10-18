def convert_to_9(number):
    s = ''
    while number:
        s = str(number % 9) + s
        number //= 9

    return s


a = []

for n in range(1000, 0, -1):
    x = convert_to_9(n)
    if x[0] == '7':
        x = x.replace('6', '*').replace('3', '6').replace('*', '3')
        x = '34' + x
    else:
        x = '3' + x[1:] + '45'
    r = int(x, 9)
    if r < 2876:
        a.append((n, r))

a.sort(key=lambda p: (p[1], p[0]), reverse=True)
print(a[0][0])
