# Check if a string is a palindrome or not.
s = input("Enter a string : ").lower() # Input from user

for char in s: # Convert to lowercase for case-insensitive comparison
    rev_s = s[::-1] # Reverse the string

if rev_s == s: # Check if the reversed string is equal to the original
    print(s,"is Palindrome") # If they are equal, it is a palindrome
else: 
    print("Not Palindrome") # If they are not equal, it is not a palindrome

# Alternative using a while loop
# s = input("Enter a string : ").lower() # Input from user
# i = 0 # Initialize index  
# j = len(s) - 1 # Last index

# while i < j: # Loop until the middle of the string

#     if s[i] != s[j]: # Compare characters from both ends
#         print("Not Palindrome") # If characters don't match, it's not a palindrome
#         break # Exit the loop
#     i += 1 # Move to the next character from the start
#     j -= 1 # Move to the next character from the end
    
# else:
#     print(s, "is Palindrome") # If loop completes, it is a palindrome
