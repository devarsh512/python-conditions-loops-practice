# #Display a pattern like this:
# 1
# 12
# 123
# 1234

n = int(input("Enter the number of rows: ")) # Input from user

for i in range(1, n + 1): # Loop from 1 to n (inclusive)
    for j in range(1, i + 1): # Loop from 1 to i (inclusive)
        print( j, end=" ") # Print numbers from 1 to i in the same line
    print() # Print a newline after each row

# Alternative using a while loop
# n = int(input("Enter the number of rows: "))  # Input from user   
# i = 1  # Start from the first row
# while i <= n:  # Loop until i exceeds n
#     j = 1  # Start from the first number in the row
#     while j <= i:  # Loop until j exceeds i
#         print(j, end=" ")  # Print the current number in the same line
#         j += 1  # Move to the next number
#     print()  # Print a newline after each row


#     1
#    1 2
#   1 2 3
#  1 2 3 4

# n = int(input("Enter the number of rows: "))  # Input from user
# for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
#     print(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))  # Print spaces and numbers for each row 
