# Anagram
# Anagram is a word created by rearranging the letters of another word

# For example, the word "Iceman" is an anagram of "Cinema" because you can rearrange the letters
# in either word to form the other

# You can determine if two words are anagrams by sorting the letters in each word alphabectically 
# and test if they are the same 

# Example of a algorithm to check anagrams

def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

result = is_anagram("iceman", "cinema")
result2 = is_anagram("iceman", "iceberg")

print(result)
print(result2)