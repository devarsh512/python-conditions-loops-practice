# Find the largest of three numbers entered by the user.
num1 = float(input("Enter first number: ")) # Input first number
num2 = float(input("Enter second number: ")) # Input second number
num3 = float(input("Enter third number: ")) # Input third number

if num1 >= num2 and num1 >= num3: # Check if num1 is the largest
    print(num1, "is the largest number.")
elif num2 >= num1 and num2 >= num3: # Check if num2 is the largest
    print(num2, "is the largest number.")
else: # If neither num1 nor num2 is the largest, then num3 is the largest
    print(num3, "is the largest number.")

