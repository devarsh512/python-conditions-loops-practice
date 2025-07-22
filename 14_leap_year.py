# Take a year as input and check if it is a leap year.
year = int(input("Enter a year: "))  # Input from user

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Check leap year conditions
    print(year, "is a leap year.")  # If conditions are met, it's a leap year
else:
    print(year, "is not a leap year.") # If conditions are not met, it's not a leap year
# Note: A year is a leap year if it is divisible by 4,
# but not divisible by 100, unless it is also divisible by 400. 