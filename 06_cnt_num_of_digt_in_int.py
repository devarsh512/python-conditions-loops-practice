# Count number of digits in an integer.

num = int(input("Enter an integer: "))  # Input from user

if num < 0:
    num = -num  # Make it positive if negative

count = 0  # Initialize digit count

if num == 0:
    count = 1  # Special case: 0 has 1 digit
else:
    while num > 0:  # Loop until num becomes 0
        count += 1  # Increment count for each digit
        num //= 10  # Remove the last digit (// : floor division)

print("Number of digits:", count)  # Output the count


#################################################
# Alternative using string conversion
# num = int(input("Enter an integer: "))  # Input from user

# # Convert to positive, then string, then count length
# count = len(str(abs(num)))

# print("Number of digits:", count)
