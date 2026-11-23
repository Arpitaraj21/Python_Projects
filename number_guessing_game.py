import random

def number_guessing_game():

    number = random.randint(1,10)

    while True:
            
        userInput = int(input("Guess the number between 1 and 100: "))

        if number <  userInput:
            print("Too high!")

        elif number > userInput:
            print("Too low!")

        else:
            print("Congratulations! You guessed the number.")


number_guessing_game()