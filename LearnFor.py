# Q1 - Practice: Define a function “print_list” that accepts a list of strings and, for all strings, prints the string.
def print_list(lst):
 for letter in lst:
    print(letter)

#print_list(["Jonny", "Mawan"])
# Q2 - Quiz: Define a function “print_gt3” that accepts a list of numbers and, for all numbers, prints whether it is greater than 3 or not.
def print_gt3(lst):
  for number in lst:
    print(number > 3)

#print_gt3([2, 5, 7])
# Q3 - Quiz: Define a function “print_add3” that accepts a list of numbers and, for all numbers, prints 3 more than the number.
def print_add3(x):
  for i in x:
    print(i+3)
    
#print_add3([2, 5, 7])
# Q4 - Practice: Define a function “print_a_names” that accepts a list of names and, for all names, prints the name only if the name starts with an “A”. 
# Hint: The string method “startswith” accepts 1 string argument and checks if the string starts with that argument.
def print_a_names(lst):
  for name in lst:
    if name.startswith("A"):
      print(name)

#print_a_names(["Agis", "Ahmad", "Surya"])
# Q5 - Quiz: Define a function “print_nums_gt3” that accepts a list of numbers and only prints numbers greater than 3.
def print_nums_gt3(lst):
  for number in lst:
    if number > 3:
      print(number)

#print_nums_gt3([2, 5, 8])
# Q6 - Practice: Define a function “get_name” that accepts a list of names and returns the first name that starts with “A”.
def get_name(names):
  for name in names:
    if name.startswith("A"):
      return name

#get_name(["David", "Ahmad", "Surya"])
      
# Q7 - Quiz: Define a function “get_odd” that accepts a list of numbers and returns the first number that is odd.
# Hint: You can check if a number is odd by using “x % 2 == 1”. The “%” is a modulo operator, so “x % 2” is 0 if x is even and 1 if x is odd.
def get_odd(number):
  for num in number:
    if num%2==1:
      return num

get_odd([4, 8, 9, 5])
