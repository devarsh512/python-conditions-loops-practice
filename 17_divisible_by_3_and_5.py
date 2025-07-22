# Print all numbers divisible by 3 and 5 between 1 to 100.
for num in range(1, 101): # Loop through numbers from 1 to 100
    if num % 3 == 0 and num % 5 == 0: # Check if the number is divisible by both 3 and 5
        print(num) # If it is, print the number
# Note: A number is divisible by another if the remainder of the division is zero.  
# In this case, we are looking for numbers where both conditions hold true.
# This will print all numbers between 1 and 100 that are divisible by both 3 and 5.