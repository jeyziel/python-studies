def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        recurse = fatorial(n-1)
        result = n * recurse
        return result

print(fatorial(3))
