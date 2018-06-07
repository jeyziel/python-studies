## 0, 1, 1, 2, 3, 5, 8
def my_fib(n):
    a = 0
    b = 1
    for i in range(n - 1):
        fib = a + b
        a = b
        b = fib
    return fib


def fib(n):
    a,b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        print(a)
        i += 1
    return a

def fib_recursive(n):
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


print(my_fib(3))
