def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def is_palindrome(word):
    length = len(word)

    for i in range(length // 2):
       if not word[i] == word[length - (i+1)]:
           return False
    return True

def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome_recursive(middle(word))


print(is_palindrome('anna'))
print(is_palindrome_recursive('allen'))
print(is_palindrome_recursive('bob'))
print(is_palindrome_recursive('otto'))
print(is_palindrome_recursive('redivider'))

