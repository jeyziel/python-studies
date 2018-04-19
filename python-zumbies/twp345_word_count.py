import string

file_ = open('alice.txt')
text = file_.read()
text = text.lower()

for c in string.punctuation:
    text.replace(c, ' ')

text = text.split()
dic = {}

for word in text:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print ('Alice aparece %s vezes' %dic['alice'])
file_.close()