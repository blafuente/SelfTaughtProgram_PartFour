# Python has a built-in function called "zip"
# Comines lists
# Zip takes zero or more iteratebles such as lists and returns a new list
# of combined tuples 

movies = [
    "Intersteller",
    "Inception",
    "The Prestige",
    "The Dark Knight",
    "Batman Begines"
]
ratings = [1, 10, 10, 8, 6]

new_list = []

for tree in zip(movies,ratings):
    new_list.append(tree)

print(new_list)

# If the lists do not contain the same number of elements
# zip outputs only tuples for which there elements in both lists

