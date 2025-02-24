'''
def my_function():
  print("Hello from a function")

my_function()
'''
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
'''
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
'''

'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
  print("The Oldest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus" )
'''


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Write a Python function that takes a list of numbers as input and returns the sum of only the even numbers in the list.