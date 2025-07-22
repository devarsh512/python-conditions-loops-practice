# Calculate the sum of digits of a number. 
num = int(input("Enter a number: "))  # Input from user

sum_of_digits = 0  # Initialize sum of digits
digits = str(num)  # Convert number to string to iterate over digits

for digit in digits:  # Loop through each digit
    sum_of_digits += int(digit)  # Convert digit back to int and add to sum
print("Sum of digits of", num, "is:", sum_of_digits)  # Output the sum of digits

# Alternative using a loop to sum digits

# num = int(input("Enter a number : "))

# for num in range(1, num+1):
#     sum_of_digits = 0
#     digits = str(num)

#     for digit in digits:
#         sum_of_digits += int(digit)

# print("Sum of digits of",num,"is : ", sum_of_digits)
