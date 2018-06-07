
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def invert_dict(d):
    dic = {}
    for key in d:
        val = d[key]
        if val not in dic:
            dic[val] = [key]
        else:
            dic[val].append(key)
    return dic

h = histogram('parrot')
print(h)

invert = invert_dict(h)
print(invert.get(1))
