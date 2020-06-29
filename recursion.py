# Recursion is a method of solving problems by breaking the problem up 
# into smaller and smaller pieces until it can be easily solved. 

# Iterative algorithms solve problems by repeating steps over and over, 
# typically using a loop

# Recursive algorithms rely on functions that call themselves

# **** Any problem you can solve iteratively can be solved recurisvely
# Sometimes a recursive algorithm is a more elegant solution

# You write a recursive algorithm inside of a function
# The function must have a base case
    # A condition that ends a recursive algorithm to stop it from continuing forever

# Three Laws of recursion :
# 1. A recursive algorithm must have a base case.
# 2. A recrusive algorithm must change its state and move toward the base case.
# 3. A recrusive algorithm must call itself, recursively. 

#Example

def bottles_of_beer(bob):
    # this satisfies the first law of recursion
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return
        # When bob is bob<1, the function returns and stops calling itself

    tmp = bob 
    
    bob -= 1 # This satisfies the second law because decrement the variable Bob moves toward 
             # your base case of bob being less than 1

    print("""{} bottles of beer on the wall. {} bottles of beer.
    Take one down, pass it around, {} bottles of beer on the wall. """.format(tmp,tmp,bob))

    bottles_of_beer(bob)
    # The third law is satisfied when you call your function.
    # This line ensures as long as your base case is not satisfied, your function will call itself.
    # Each time the function calls itself, it passes itself "bob" decremented by 1 as a parameter which
    # moves your algorithm toward your base case. 

bottles_of_beer(10)

# another example
def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n-1)

print_to_zero(5)