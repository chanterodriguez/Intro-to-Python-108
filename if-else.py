"""
An if-else statement in python is a conditionsal control structure that lets you 
decide which block of code to run depending on wheather a condition is True or False.
The if block runs only if the condition evaluates to True.
- If the condition is False, the else block runs instead
- You can also add elif (else if) blocks to check multiple conditions in a sequence
if condtition:
    - Code block runs if condition is true
elif another_condition:
    - Code block runs if the first condition is False
    - and this condition is True
else:
    - Code block always runs if none of the above conditions are True
"""

x = 7

if x >= 10:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand IF statements. (it is preferred to use the long version instead)

if x > 5: print("x is greter than 5")

# Short hand IF .... ELSE (use this for quick checks)
print("Even") if x % 2 == 0 else print ("Odd")

# Nested IF statements
x = 21
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions
age = 23

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")

    """
Mini challenge
Ask the user to enter a number from 0-100 and store it in a variable called "score".
If the score is 90 or above, print "Grade: A".
If the score is between 80-89, print "Grade: B".
If the score is between 70-79, print "Grade: C".
Otherwise, print "Grade: F".
6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
 BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"
"""


# Ask the user for their dog's age in human years and convert it to an integer
score = int(input("Enter a number from 0-100: "))

if x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70:
    print("Grade: C")
else:
    print("Grade: F")

passed = score >= 70

if passed:
    print("Congratulations!")
else:
    print("Try again!")