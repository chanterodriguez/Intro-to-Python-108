"""
List store multiple items in a sinlge variable
List are crated using = []
"""

my_list = [10, 20, 30, 40, 50]
print(my_list)

# Can contain differnt data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing itme by INDEX
# indexing starts at 0

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
print(fruits[0])

# you can use NEGATIVE indexes to count from the END
print(fruits[-1])
print(fruits[-3])

# Modifiying List items
fruits[1] = "mango" #change banana to  mango"
print(fruits)

#Adging Items
fruits.append("orange") # adds ONE item to the END of the list at a time
print(fruits)

fruits.insert(1, "kiwi") # adds before the index
print(fruits)

fruits.extend(["grape", "pear"]) # adds MULTILE items to the end of the list
print(fruits)

#Remove Items
fruits.remove("apple") #Remove by the exact VALUE (the first match it finds)
print(fruits)

fruits.pop() #Removed the LAST item in a list
print(fruits)

fruits.pop(3) #Removed the SPECIFIC index
print(fruits)

#fruits.clear() #Removed the list leaving it empty []
#print(fruits)

# Looping through a list
for x in fruits:
    print(x)

# Checks if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

#List length
print(len(fruits)) #Number of items in list

# Slicing a list
# Slicing let syou grab a RANGE of items using [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  #index 2 - 5
print(numbers[:4])   #start from the very beginning up to index 4
print(numbers[6:])   #starts at index 6 till the end of list
print(numbers[-3:])  #returns last 3 items
print(numbers[::2])  #step skips every 2nd item


#useful list methods
numbers = [4, 2, 9, 1, 7]

print(numbers.count(2)) # counts number of times the item is in the list
print(numbers.index(9)) # Returns the index where the item first appears

numbers.sort()          # Sorts the list in place (smallest to largest)
print(numbers) 

numbers.sort(reverse=True) # Sorts the list in place (largest to smallest)
print(numbers)

numbers.reverse() # flips current order of the list
print(numbers)

number_copy = numbers.copy() # makes a real COPY of the list
print(number_copy)

"""
-------------------------------
MINI CHALLENGE: HIGH SCORE BOARD
-------------------------------
You are building a leaderboard for a game.

1. Create a list called "scores" with at least 6 integer scores.
2. Use a list comprehension to create "bonus_scores" where every
   score has 10 points added to it.
3. Sort "bonus_scores" from highest to lowest.
4. Print the TOP 3 scores using slicing.
5. Use count() to check how many times a specific score appears.
6. Remove the LOWEST score from the list using pop() and the index
   of the minimum value (hint: use .index(min(list))).
7. Print the final list and how many scores remain.
"""

# -------------------------------
#  MINI CHALLENGE: THE GROCERY LIST
# -------------------------------
# You're building a grocery list app.
# 1. Create a list called "groceries" with at least 5 items.
# 2. Print the first and last item using indexing.
# 3. Use slicing to print just the first 3 items.
# 4. Add "eggs" to the end of the list using append().
# 5. Insert "milk" at the very beginning of the list.
# 6. Remove one item using remove().
# 7. Check if "bread" is in the list — print a message either way.
# 8. Sort the list alphabetically and print it.
# 9. Print how many items are in the final list.


groceries = ["bread", "apples", "cheese", "bananas", "chicken"]

print("First item:", groceries[0])
print("Last item:", groceries[-1])
print("First 3 items:", groceries[:3])

groceries.append("eggs")
print(groceries)

groceries.insert(0, "milk")
print(groceries)

groceries.remove("cheese")
print(groceries)

if "bread" in groceries:
    print("Bread is on the list!")
else:
    print("Bread is not on the list.")

groceries.sort()
print("Sorted list:", groceries)

print("Total items:", len(groceries))