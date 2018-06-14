
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

t1 = [1,2,3,4,5,6,7,8,9]
t2 = [10, 20, 3, 15, 16,17, 25]
print(has_match(t1, t2))

for index, value in enumerate([1,2,3,4,5,6,7]):
    print(index, value)
