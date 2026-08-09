# Ask the user for their dog's age in human years and convert it to an integer
human_age = int(input("Enter your dog's age in human years: "))

# Calculate the dog's age in dog years
dog_age = dog_human_age * 7

# Display the result using an f-string
print(f"Your dog is {dog_age} years old in dog years!")