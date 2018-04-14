list = [1,2,3,4,5,6]

for item in list:
    print(item)

for item in list[0:3]:
    if item > 2 :
        print('greater than 2')


words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))


# Loop over a slice copy of the entire list.     
for w in words[:]:
    if (len(w) > 6):
        words.insert(0, w)

print(words)        