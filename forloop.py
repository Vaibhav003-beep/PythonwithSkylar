'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
'''

'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''
#Write a Python program that takes a list of numbers and prints whether each number is even or odd using a for loop.

numbers = [12, 7, 19, 24, 5, 8, 30]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")