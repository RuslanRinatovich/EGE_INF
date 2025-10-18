for n in range(1, 200):
    x = f'{n:b}'
    if n % 3 == 0:
        x = x + x[-3:]
    else:
        a = n % 3 * 3
        x = x + f'{a:b}'
    r = int(x, 2)
    if r >= 200:
        print(n)
        break
