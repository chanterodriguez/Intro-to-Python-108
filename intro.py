print("Hello World from Python!")
print(2)
print(5 + 3)
print(True)

# SHORTCUTS:
# save file: ctrl + s windows| cmd+s mac
# up on arrow key gose to previous commands

# SINGLE LINE Comments

"""
Multi line make sure to use 3 quotes before and after 
"""
'''
this works too with single quotes
'''

# Variables and Concatenation
name = "Leo"
age = 28
print(name, age)

# you cannot concatinate an interger with a string
print("My name is " + name + " and I am " + str(age) + " years old. ")

"""
Mini - Callenge 
Write a short story using variables.
1. Declare and initialize 5 variables (strings and numbers)
2. use print() and concatenation to tell a story
3. run the program in terminal
"""

name = "Chante'"
likes = "swimming"
age = 44
pets = "dogs"
pet_count = 3

print("My name is " + name + " and I am " + str(age) + " years old. In the summer I enjoy " + likes + ". I also enjoy my " + str(pet_count) + " " + pets + ".")


#F-String
print(f"My name is {name} and I am {age} years old. In the summer I enjoy {likes}. I also enjoy my {pet_count} {pets}.")

#Multi-line f-String
print(f"""My name is {name} and I am {age} years old. 
            In the summer I enjoy {likes}. 
    I also enjoy my {pet_count} 
    {pets}.""")

# Type Function
print(type(name)) #string
print(type(age)) # int
print(type(False)) # bool

#Casting (chanign datea types)
print(20 + int("20"))
print(20 + age)

# User Input Function
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# input() always returns a sting
# print(type(input("Enter your name: ")))

# new_age = int(input("Enter your age: "))
# print(age + new_age)

"""
Mini - Callenge 
Pizza Calculator
1. Ask how many slices of pizza and how many people.
2. Use math operators to calculate slices per person. (divide /)
3. Show the results with an f-string
"""

slice_count = int(input("How many slices of pizza are there?"))
people_count = int(input("How many people are there?"))
slice_per_person = slice_count / people_count
print(f"Each person get {slice_per_person} slices of pizza")