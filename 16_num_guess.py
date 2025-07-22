# Create a number guessing game using a while loop.
import random  # Importing the random module to generate a random number
number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
attempts = 0  # Initialize the number of attempts   
while True:  # Start an infinite loop
    guess = int(input("Guess a number between 1 and 100: "))  # Input from user
    attempts += 1  # Increment the number of attempts
    if guess < number_to_guess:  # If the guess is too low
        print("Too low! Try again.")  # Prompt to try again
    elif guess > number_to_guess:  # If the guess is too high
        print("Too high! Try again.")  # Prompt to try again
    else:  # If the guess is correct
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")  # Output success message
        break  # Exit the loop when guessed correctly
# Note: The game continues until the user guesses the correct number.