# Count how many times a letter appears in a string using a loop.
s = input("Enter a string: ").lower()  # Input from user
letter = input("Enter a letter to count its appearances: ").lower()  # Input the letter to count
count = 0  # Initialize count variable
for char in s:  # Loop through each character in the string
    if char == letter:  # Check if the character matches the input letter
        count += 1  # Increment count if it matches
print(f"The letter '{letter}' appears {count} times in the string.")  # Output the count
# Note: This code counts the occurrences of a specific letter in a given string.