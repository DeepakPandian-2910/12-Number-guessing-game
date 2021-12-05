import random
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    no_of_tries = 10
else:
    no_of_tries = 5
while no_of_tries > 0:
    print(f"You have {no_of_tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The number was {chosen_number}")
        break
    elif guess < chosen_number:
        print("Too low.")
    else:
        print("Too high.")
    no_of_tries -= 1
    if no_of_tries > 0:
        print("Guess again.")
if no_of_tries == 0:
    print("You've run out of guesses, you lose.")
