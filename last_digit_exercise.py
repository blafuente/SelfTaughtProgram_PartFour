# Use a list comprehension to turn [1, 7, 5, 3, 2] into a new list. The new list should contain all the integers
# in the original list multiplied by 7. Then, print your new list.

my_list = [1, 7, 5, 3, 2]
new_list = [num*7 for num in my_list]
print(my_list)
print(new_list)