# Q1 - Practice: Define a function “mul3” that accepts a number argument and returns that number multiplied by 3.
def mul3(x):
    return x*3

# Q2 - Quiz: Define a function “sub3” that accepts a number argument and returns that number subtracted by 3.
def sub3(x):
    return x-3

# Q3 - Practice: Define a function “prod” that accepts two number arguments and returns the product of both numbers.
def prod(x, y):
    return x+y

# Q4 - Quiz: Define a function “add” that accepts two number arguments and returns the sum of both numbers.
def add(x, y):
    return sum(x, y)

# Q5 - Quiz: Define a function “prod” that accepts three number arguments and returns the product of all 3 numbers.
def prod3(x, y, z):
    return x+y+z

# Q6 - Practice: Define a function “gt3” that accepts a number argument and returns whether or not the number is greater than 3.
def gt3(x):
    return x>3

# Q7 - Quiz: Define a function “lt10” that accepts a number argument and returns whether or not the number is less than 10.
def lt10(x):
    return x<10

# Q8 - Quiz: Define a function “both_gt_3” that accepts two number arguments and returns whether or not both numbers are greater than 3.
# Hint: Recall “x and y” will return whether both “x” and “y” are True
def both_gt_3(x, y):
    return x>3 and y>3

# Q9 - Practice: Define a function “sum3” that accepts a list of numbers and returns the sum of that list, multiplied by 3.
def sum3(x):
    return sum(x)*3

# Q10 - Quiz: A dictionary method “values” returns all values in the dictionary. Define a function “sumv” that accepts a dictionary and returns the sum of all values in that dictionary. Use “sumv” to compute the sum of all values in {“a”: 1, “b”: 2}.
def sumv(dictionary):
    return sum(dictionary.values())

# Q11 - Practice: Define a function “is_jack_one” that accepts a dictionary as input and checks if the number corresponding to “jack” in the input dictionary, is 1.
def is_jack_one(dictionary):
    return dictionary["jack"]==1

# Q12 - Quiz: Define a function “add3_jack” that accepts a dictionary as input and returns 3 more than the number corresponding to “jack” in the input dictionary.
def add3_jack(dictionary):
    return dictionary["jack"]+3
