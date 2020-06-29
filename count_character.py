# Another popular interview question is to count how many times each 
# character occurs in a string

def count_characters(string):

    count_dict = {}
    
    # going thru each character in the string
    for c in string:
        # if its in your dictionary, increment its value
        if c in count_dict:
            count_dict[c] += 1
        # otherwise it has a key of one
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("hello")
count_characters("racecar")