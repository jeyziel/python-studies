import re

text ="'I AM NOT YELLING', she said. Though we knew it to not be true"

new = re.sub('[a-z]', '', text)


print(text)
print(new)