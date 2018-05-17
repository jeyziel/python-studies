def fibonnaci(n):
    a = 0
    b = 1
    while b < n:
        a, b = b, a + b
    print(b)

def fibonnaci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci_recursive(n-1) + fibonnaci_recursive(n - 2)

fibonnaci(5)

print(fibonnaci_recursive(8))