# Find the factorial of a number provided by the user.
num = int(input("Enter a number : ")) # Input a number from the user
fact = 1 # Initialize factorial to 1
for i in range(1,num+1): # Loop from 1 to the number+1 
    fact *= i # Multiply the current value of fact by i
    #fact = fact * i # Alternative way to calculate factorial
print("The factorial of", num, "is", fact) # Print the factorial of the number
# End of the program

# using while loop
# num = int(input("Enter a number : ")) # Input a number from the user
# fact = 1 # Initialize factorial to 1
# i = 1 # Initialize i to 1
# while i <= num: # Loop until i is greater than the number
#     fact *= i # Multiply the current value of fact by i
#     i += 1 # Increment i by 1
# print("The factorial of", num, "is", fact) # Print the factorial of the number





