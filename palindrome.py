# Palimdrome Algorithm
# A palimdrome is a word spelled the same way forward and backward

def is_palimdrome(word):
    # python treats upper and lower case letters differently
    word = word.lower()
    # returns True or False
    return word [::-1] == word

result = is_palimdrome("racecar")
result2 = is_palimdrome("mom")
result3 = is_palimdrome("mother")

print(result)
print(result2)
print(result3)