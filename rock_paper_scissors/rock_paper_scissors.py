import random


def play():
    player = input("Please select your move by entering 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return "Wow 😳, It's a Tie!"

    if is_win(player, computer):
        return "Yay 🎉, You Win!"

    return "Oops 😔, You lose!"


def is_win(player, opponent):
    if ((player == 'r' and opponent == 's')
            or (player == 'p' and opponent == 'r')
            or (player == 's' and opponent == 'p')):
        return True


print(play())
