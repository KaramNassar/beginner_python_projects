from user_guess import user_guess
from computer_guess import computer_guess

play = "y"
while play == "y":
    who_is_guessing = input("Please select an option:\n"
                            "1. Enter '1' if you want to guess the number.\n"
                            "2. Enter '2' if you want the computer to guess the number.\n"
                            "Enter your choice: ")
    highest = int(input("Please enter the highest limit for the range: "))

    if who_is_guessing == "1":
        user_guess(highest)
    elif who_is_guessing == "2":
        computer_guess(highest)
    else:
        print("Error: Please enter either '1' or '2'.")

    play = input("Would you like to play again?\n"
                 "Enter 'Y' to play again, or any other key to exit: ").lower()
