import random  # Import the random module to generate random numbers

num = random.randint(1, 10)  # Generate a random number between 1 and 10
guess = int(input("Make a guess: "))  # Ask the user for their guess and convert it to an integer
print(num)  # Print the random number (for debugging purposes)
count = 1  # Initialize the count of attempts

# Continue looping until the user's guess is equal to the random number
while guess != num:
    print("Wrong guess. Please try again.")  # Inform the user that the guess was incorrect
    count += 1  # Increment the attempt count
    guess = int(input("Make a guess: "))  # Ask for another guess

# Inform the user that they guessed correctly
print(f"Correct guess! The number was: {num}")  
# Print the total number of attempts the user made
print(f"Total attempts: {count}")  
