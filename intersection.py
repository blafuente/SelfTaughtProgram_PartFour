# Find the intersection of two lists

# Goal is to find elements common to both lists. 

# Create a function that look to see if values in list_1 are also in list_2
def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

print(intersection(list1,list2))

# Python has a built-in intersection function to return an elelments that appear into or more sets.
# The intersection function works for sets, not for lists
# A set is a data structure that is a collection of unique unordered immutable objects
# Example:
# set(2, 43, 48, 62, 64, 28, 3)
# set(2, 2, 48, 62,64, 28, 3) - this cannot be a set 
# The elements of a set are enlocsed in paranthesis.
# Unlike a list or tuple, a set cannot have multiple occurences of the same element. 

# Can easily change lists into sets like this
# set1 = set(list1)
# set2 = set(list2)
# Once you converted the lists to sets, you can apply the intersection function to find out 
# where the two sets have items that are the same
# It's syntax looks like this

# set1.intersection(set2)
#convert back in to a list using a list function
# list(set1.intersection(set2))

# Putting it together

def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
new_list = return_intersection(list1, list2)
print(new_list)

# (set1.intersection(set2,set3,set4))
# This helps find the intersection of multiple sets