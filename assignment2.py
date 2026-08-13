#You must create a new list (not the one from the example), just like we practiced in class.

# 1. Creating a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# 2. Accessing items by index
first_item = fruits[0]
print(first_item)

# 3. Replacing values
fruits[1] = "blueberry"
print(fruits)

# 4. Removing an item by value
fruits.remove("cherry")
print(fruits)

# 5. Removing an item by index
removed_item = fruits.pop(0)
print(removed_item)
print(fruits)

# 6. Printing the list and its length
print(fruits)
print(len(fruits))


#You must create a new dictionary with your own values, following the same structure we used in class.

# 1. Creating a dictionary with key:value pairs
student = {
    "name": "Chante",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.8
}
print(student)
print(len(student))

# 2. Accessing values using keys
name_value = student["name"]
major_value = student["major"]
print(name_value)
print(len(student))

# 3. Adding new keys
student["graduation_year"] = 2027
print(student)
print(len(student))

# 4. Updating existing values
student["gpa"] = 3.9
print(student)
print(len(student))

# 5. Removing keys
del student["age"]
print(student)
print(len(student))

# 6. Printing the dictionary and its length
print(student)
print(len(student))