

def has_duplicate(t):
    t.sort()
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def has_duplicate2(t):
    return len(set(t)) < len(t)



t = [1,3,2,4,5]
x = [1,2,3,3,4,5,7]

print(has_duplicate(t))
print(has_duplicate(x))

print(has_duplicate2(t))
print(has_duplicate2(x))
