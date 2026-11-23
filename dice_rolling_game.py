import random

def dice_rolling_game():

    while True:
        userInput = input("Roll the dice? (y/n)").lower()

        if userInput == 'y':
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)

            print((dice1, dice2))
        
        elif userInput == 'n':
            print("Thankyou for playing")
            break
    
        else:
            print("Invalid choice!")


dice_rolling_game()