# Find the sum of all prime numbers between 1 to 100
num = int(input("Enter a number: "))  # Input from user

prime_sum = 0  # Initialize sum of prime numbers

for n in range(2, num + 1):  # Loop through numbers from 2 to num
    is_prime = True  # Assume n is prime

    for i in range(2, int(n**0.5) + 1):  # Check divisibility from 2 to sqrt(n)
        if n % i == 0:  # If n is divisible by i
            is_prime = False
            break

    if is_prime:  # If n is still marked as prime
        prime_sum += n  # Add n to the sum of primes
        
print("Sum of prime numbers up to", num, "is:", prime_sum)  # Output the sum of prime numbers
# Note: A prime number is a natural number greater than 1 that cannot be formed by