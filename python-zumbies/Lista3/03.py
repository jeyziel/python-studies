a = 80.000
b = 200.000

anos = 0

while a<=b:
    a = a * 0.03
    b = b * 0.015
    anos = anos + 1
print('serão necessário %d anos' %anos)