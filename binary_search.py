# Binary Search
# Requires O(logn) time
# Binary search locates an element in a list by successfully dividing the list into halves

# Summary of Binary Search
# It is a series of iterations that divide a sorted list in half 
# to drill down to a specific element. 

#Example

def binary_search(the_list, item):
    first = 0
    last = len(the_list)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if the_list[mid] == item:
            found = True
        else:
            if item < the_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

the_list = [10, 12, 13, 14, 15, 18, 19]
item = 19  #Target Item
if binary_search(the_list, item):
    print("The item is in the list.")
else:
    print("The item is Not in the list.")