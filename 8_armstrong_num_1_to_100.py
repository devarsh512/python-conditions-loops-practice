# Print all the Armstrong numbers from 1 to 100
# An Armstrong number (or narcissistic number) is a number that is equal 
# to the sum of its own digits each raised to the power of the number of digits.
for num in range(1, 101): # Loop through numbers from 1 to 100
    sum_of_powers = 0 # Initialize sum of powers    
    digits = str(num) # Convert number to string to iterate over digits
    num_digits = len(digits) # Count the number of digits

    for digit in digits: # Loop through each digit
        sum_of_powers += int(digit) ** num_digits # Raise digit to the power of number of digits and add to sum
        if sum_of_powers > num: # If sum exceeds num, no need to check further
            break  # Exit the loop early if sum exceeds num
    
    if sum_of_powers == num: # If the sum of powers equals the number
        print(num, "is an Armstrong number") # Print the Armstrong number
