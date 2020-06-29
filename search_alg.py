# Search Algorithm
# Checks each item in a data structure to see if the item matches 
# what it is looking for

def ss(number_list, n):
    found = False 
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(1, 101)
result = ss(numbers, 50)
result2 = ss(numbers, 200)
print(result)
print(result2)
