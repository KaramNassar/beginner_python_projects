import random


def user_guess(x):
    secret_number = random.randint(1, x)
    guess = 0

    while guess != secret_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > secret_number:
            print("Oops, that's too high")
        elif guess < secret_number:
            print("Oops, that's too low")

    print(f"Yay, You guessed the number {guess} correctly!")
