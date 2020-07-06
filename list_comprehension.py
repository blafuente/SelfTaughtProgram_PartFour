# List Comprehensions
    # Allows you to create lists based on criteria applied to existing lists. 

# You can create a list comprehension with one line of code that examins every character in the original string
# Selects digigts from a string and puts them in a list. 
# Or selects the right-most digit from the list.

# Example:
# return [c for c in input_string if c.isdigigt()][-1]

input_string = "Buy 1 get 2 free"
# A simple use of list comprehension is to create a new list from a string
new_list = [c for c in input_string]
# Basically says to loop through each character in input_string to create a new list
print(new_list)

# [c for c in input_string if c.isdigit()]
# You can also add a conditional statement to the list comprehension 
# The 'if' clause only allows digits to go into the new list 
# The output will be a list containing only digits from the input_string
# You can tack on a negative index to select only the last digit from the new list. 
# [c for c in input_string if c.isdigit()][-1]

# new_list = [expression(i) for i in input_list if filter(i)]
# The general syntax for a list comprehension contains a flexible collection of tools that can be applied to lists
# Expression(i) is based on the variable used for each elelment in the input_string
# You can simply step through each item using an expression such as "c for c" or you can manipulate
# those items mathematically or character wise.

# For example, the expression price*3 for price would step through each value of price at the 
# same time multiplying each price by three. 

# The word[0] for word would step through a list of words, taking the first letter of each

# in input_list
# This part of the list comprehension specifies the input string or list the last part of the 
# list comprehension

# if filter(i)
# The last part of the list comprehension allows you to add a conditional statement to filter out list items that match 
# specified critera such as being a digit ,if c.isdigit(), or being an even number (if n%2 == 0)

# recap
# List comprehension create lists based on criteria that iterate, processes, or filters an existing list 
# The general syntax for a list comprehension statement can contain an expression for stepping through an input list 
# based on a for loop and then expression to use as a filter to select specific items from the input_list to be added 
# to the new_list