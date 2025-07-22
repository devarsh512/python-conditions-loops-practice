# Reverse a given number using loop.
num = int(input("Enter an integer: "))  # Input from user

if num < 0:
    num = -num  # Make it positive if negative  

reversed_num = 0  # Initialize reversed number

while num > 0:  # Loop until num becomes 0
    digit = num % 10 # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit (// : floor division)
print("Reversed number:", reversed_num)  # Output the reversed number


# Alternative using string conversion
# num = input("Enter an integer: ")  # Input from user
# reversed_num = num[::-1]  # Reverse the string
# print("Reversed number:", reversed_num)  # Output the reversed number


