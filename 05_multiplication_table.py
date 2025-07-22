# Print the multiplication table of a number.
num = int(input("Enter a number : "))  # Input from user

for i in range(1,11): # Loop from 1 to 10
    print(num, "x", i, "=", num * i) # Print the multiplication result

# using while loop
# num = int(input("Enter a number: "))  # Input from user
# i = 1 # Start from 1
# while i <= 10:  # Loop until 10
#     print(num, "x", i, "=", num * i)  # Print the multiplication result
#     i += 1  # Increment i by 1