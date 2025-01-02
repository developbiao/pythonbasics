from functools import reduce

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x * x

# Use map to apply hte square function to each item in the list
squared_numbers = list(map(square, numbers))
print("Squared numbers:", squared_numbers)

# Define a function to sum two number
def add (x, y):
    return x + y
# Use reduce to sum all the squared numbers
sum_of_squares = reduce(add, squared_numbers)
print("Sum of squared numbers:", sum_of_squares)

