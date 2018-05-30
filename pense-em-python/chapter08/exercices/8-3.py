def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome('aba'))
print(is_palindrome('abc'))
print(is_palindrome('arara'))