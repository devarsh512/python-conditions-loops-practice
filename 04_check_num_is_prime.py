# Check if a number is prime or not
num = int(input("Enter a number: "))  # Input from user

if num == 1:
    print("1 is not a prime number")  # Special case
else:
    i = 2                             # Start checking from 2
    is_prime = True                   # Assume the number is prime

    while i <= num**0.5:              # Check up to the square root of num
        if num % i == 0:              # If divisible by i
            is_prime = False          # It's not a prime
            break                     # Exit the loop
        i += 1                        # Go to next i

    if is_prime and num > 1:          # If still marked prime and >1
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
