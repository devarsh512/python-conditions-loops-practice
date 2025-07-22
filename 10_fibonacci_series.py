# Print the Fibonacci sequence up to n terms.
n = int(input("Enter a num : ")) # Input from user

a, b = 0, 1 # Initialize the first two Fibonacci numbers

print("Fibonacci sequence up to", n, "terms:") # Print the header

for i in range(n): # Loop n times
    print(a, end=" ") # Print the current Fibonacci number.(end=" " : print output in horizontal line)
    a, b = b, a + b # Update to the next Fibonacci numbers

print() # Print a newline at the end

