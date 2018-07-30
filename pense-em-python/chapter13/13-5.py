import random

def histogram(t):
    d = {}
    for word in t:
        d[word] = d.get(word, 0) + 1
    return d

def choose_from_hist(hist):
    random_choice = random.choice(list(hist.keys()))
    sum_of_hist = sum(hist.values())
    return 'A probabilidade da palavra {} aparecer é de : {} / {}'\
    .format(random_choice, hist[random_choice], sum_of_hist )

t = ['a', 'a', 'b']
hist = histogram(t)
choose = choose_from_hist(hist)
print(choose)
