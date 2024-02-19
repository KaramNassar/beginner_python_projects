import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess = 0

    while feedback != "c":
        if low == high:
            guess = low
        else:
            guess = random.randint(low, high)

        feedback = input(f"Is the {guess} too high(H), too low(L) or corrct(C): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Wow, The computer guessed the number {guess} correctly!")
