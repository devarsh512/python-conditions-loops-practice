# Take an integer and print whether it is even or odd.
num = int(input("Enter an integer: ")) # Input from user

if num % 2 == 0: # Check if the number is even
    print(num, "is an even number.") # If even, print this
else: # If not even, it is odd
    print(num, "is an odd number.") # If odd, print this
# Note: An even number is divisible by 2, while an odd number is not.