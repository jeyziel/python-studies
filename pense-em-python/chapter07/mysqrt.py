def mysqrt(a, x):
    while True:
        y = (x + a / x) / 2
        print(y)
        if abs(y - x) < 0.0000001:
            break
        x = y

mysqrt(9, 4)