

def uses_only(word, availlable):
    for letter in word:
        if letter not in availlable:
            return False
    return True


print(uses_only('hoealfafa','acefhlo'))