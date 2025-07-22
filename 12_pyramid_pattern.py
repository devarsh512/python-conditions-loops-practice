# Print a pyramid pattern using asterisk(*) of height n.
n = int(input("Enter the height of the pyramid: ")) # Input from user
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    print(' ' * (n - i) + '*' * (2 * i - 1))  # Print spaces and asterisks for each row
    
# using a while loop
# n = int(input("Enter the height of the pyramid: "))  # Input from user
# i = 1  # Start from the first row
# while i <= n:  # Loop until i exceeds n
#     print(' ' * (n - i) + '*' * (2 * i - 1))  # Print spaces and asterisks for the current row
#     i += 1  # Move to the next row
