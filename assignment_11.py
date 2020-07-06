# Assignment during lesson

# Given a non-empty list of integers, every element appears twice except for one. 
# Find that single one.

# Scan through list, find a way to find the single element. 
# Would converting in the list into set work? 

list_of_integers = (1, 1, 2 ,2 ,3 ,3 ,4 ,5 ,5 ,6 ,6 ,7 ,7)
some_dict = {}
for num in list_of_integers:
        if num in some_dict:
            some_dict[num] += 1
        else:
            some_dict[num] = 1

print(some_dict)


my_dict = {"one": 1,"two":2,"three":3,"four":4}

for item in some_dict:
    if some_dict[item] == 1:
        print(item)


# Combining the lines to small section-ish
list_of_integers = (1, 1, 2 ,2 ,3 ,3 ,4 ,5 ,5 ,6 ,6 ,7 ,7)
some_dict = {}
for num in list_of_integers:
        if num in some_dict:
            some_dict[num] += 1
        else:
            some_dict[num] = 1
for single_out in some_dict:
    if some_dict[single_out] == 1:
        print(single_out)