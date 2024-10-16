import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            attempts -= 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess}.")
                break
            
            if attempts == 0:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
