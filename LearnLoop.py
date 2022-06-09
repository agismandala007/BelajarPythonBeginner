# Q1 - Practice: Define a function “gt5” that accepts 1 number argument; if that argument is greater than 5, return “yay!”.
def gt5(x):
  if x > 5:
    return "yay!"

# Q2 - Quiz: Define a function “reaction” that accepts 1 string argument; if that argument is “among us”, return “yay!”.
def reaction (dictionary):
  if dictionary=="among us":
    return "yay! "

# Q3 - Practice: Define a function “gt5o” that accepts 1 number argument; if that argument is greater than 5, return “yay!”. Otherwise, return “nu!”
def gt5o (x):
  if x>5:
    return "yeay! "
  else:
    return "nu! "

# Q4 - Quiz: Define a function “reaction” that accepts 1 string argument; if that argument is “among us”, return “yay!”. Otherwise, return “nu!”
def react1on(dictionary):
  if dictionary == "among us":
    return "yay!"
  else:
    return "nu!"

# Q5 - Practice: Define a function “blackjack” that accepts a list of numbers. If the sum of the numbers is less than 21, return the sum. Otherwise, return 0.
def blackjack(number):
  if sum(number)<21:
    return sum(number)
  else:
    return 0

# Q6 - Quiz: Define a function “can_cook” that accepts a list of strings. If the list of strings contains “lemon”, return the list. Otherwise, return an empty list. (Hint: “hello” in lst will return True if the variable “lst” contains the string “hello”)
def can_cook(daftar):
  if "lemon" in daftar:
    return daftar
  else:
    return []
# Q7 - Quiz: Define a function “laugh” that accepts a list of booleans. If any of the booleans are True, return “haha”. Otherwise, return “uh”. (Hint: the any function will return True if any boolean in the input list is True)
def laugh(lst):
  if any(lst):
    return "haha"
  else:
    return "uh"
      
#Q8 : Write a while loop that prints every number from 5 to 10.
def loop():
  x=5
  while x <= 10:
    print(x)
    x+=1

# Q9 - Quiz: Write a while loop that prints every odd number from 5 to 15.
def oddnumber():
  x=5
  while x<=15:
    if x%2!=0:
      print(x)
    x+=1

# Q10 - Quiz: Write a function “print_from_to” that accepts two number arguments and prints every number from the first argument to the second. For example, “print_from_to(3, 6)” would print all numbers from 3 to 6.
def print_from_to(x, y):
  while x <= y:
    print(x)
    x += 1

# Q11 - Practice: Write a while loop that prints every number from 5 to 10 that is not a multiple of 3 (Hint: Use if statement)
def lo0p():
  x=5
  while x<=10:
    if x % 3!=0:
      print(x)
    x+=1

# Q12 - Quiz: Write a while loop that prints every number from 5 to 15 that is not a multiple of 6. (Hint: Use if statement)
def lo0p6():
  x=5
  while x<=15:
    if x%6 != 0:
      print(x)
    x+=1
