#Arithmetic operators - used with numeric values to perform common math operations

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y  # multiplication
print(res)

res = x / y  # division
print(res)

res = x % y  # MODULUS - removes the remainder after division
print(res)

res = x ** y # Exponentation -> x to the power of y
print(res)

res = x // y # FLOOR DIVISION - divide and drop the decimal
print(res)

# Assignment operator - used to assign values to variables
# +=, -=, *=, /=

x = 5
x += 5
x -= 3
x *= 3
x /= 2
print(x)

#comparison operator - used to compare
# == (Equal to), != (not equal to), < > (greater than/less than) <= >=

# Logical Operator- used to combine conditional statements
# used with True/False value like conditions
# and -> both must be True
# or -> at least one must be True
# not -> flips True to False (vice versa)


x = 3
y = 10
z = 10

print( x == y and z == y ) # False, because both conditions are NOT true
print( x == y  or y == z ) # True, because at least one condition is True
print(not x == y) #True, becuase x is not equl to y

# Identity operator- used to compare the objects, not if they're equal but
# if they're actaully the same object with the same memory location
# is -> check if two things are the exact same
# is not -> Checks if they are NOT the same

x = 3
y = 3
print( x is y ) #Returns true if both variables are the same object
print( x is not y )  #Returns true if both variables are Not the same object

# Membership Operator - used to test if a sequence is presented in an object
# in -> checks if something exists inside a sequence (list, string, etc...)
# not in -> checks if something does NOT exist inside

x = [1, 2, 3, 4, 5]

print(4 in x) # True, because 4 is inside the list
print(9 not in x) # True, because 9 is NOT inside the list