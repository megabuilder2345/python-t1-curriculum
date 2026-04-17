# Problem 1
# Write a function that returns the number 42 and print the result.
def x():
    return "42"

y=x() 
print(y)


# Problem 2
# Write a function that returns "penguin" and print the result.
def p():
    return "penguin"

q=p() 
print(q)


# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = "apple"
print(fruit)
def fruit():
    fruit = "mango"
    print(fruit)

# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
def name(first_name, last_name):
    fullname=(first_name + last_name)
    return fullname
print(name("bob ","bobby"))


# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def rectangle_perimeter(length,width):
    perimeter=(2 * (length + width))
    return perimeter

print("the perimeter of a 5x3 rectangle is:", rectangle_perimeter(5,3))