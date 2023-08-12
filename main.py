# FOR LOOP 

nick_names = ["yo", "hello", "idk"]

for nick_name in nick_names:
  print(f"ramdom words :- {nick_name}.")

# finding highest score using for loop

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

x = 0
for score in student_scores:
 if score > x:
    x = score
print(f"The highest score in the class is: {x}")

# FOR loop with Range function

total = 0

for num in range(1, 101):
  total += num
print(total)

# Using 3 parameter of range
# add even number

even_total = 0
for num in range(1, 101):
  if num % 2 == 0:
    even_total += num
print(even_total)

# FizzBuzz

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)

# password Generator

import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the MyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_list = []

for char in range(1, nr_letters + 1):
  password += random.choice(letters)
  password_list += random.choice(letters)
  
for symbol in range(1, nr_symbols + 1):
  password += random.choice(symbols)
  password_list += random.choice(symbols)
  
for num in range(1, nr_numbers + 1):
  password += random.choice(numbers)
  password_list += random.choice(numbers)


random.shuffle(password_list)

hard_password = ""
for char in password_list:
  hard_password += char


print(f"Here is your easy password :- {password}")
print(f"Here is your hard password :- {hard_password}")

