a = 4
x = 3
y = 0

epsilon = 0.0000001

while True:
    y = (x + a / x) / 2
    print(y)
    
    if abs(y-x) < epsilon:
        break
    x = y
    


