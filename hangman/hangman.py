import random
import string

from hangman_visual import lives_visual_dict
from words import words


def get_valid_word():
    word = random.choice(words)
    while "_" in word and " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left, and you have used these letters: {" ".join(used_letters)}")

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(lives_visual_dict[lives])
        print(f"Current word: {" ".join(word_list)}")

        player_letter = input("Guess a letter: ").upper()
        if player_letter in alphabet - used_letters:
            used_letters.add(player_letter)
            if player_letter in word_letters:
                word_letters.remove(player_letter)

            else:
                lives -= 1
                print(f"You're letter {player_letter} is in not in the word 😢")

        elif player_letter in used_letters:
            print("You've already used that letter.")

        else:
            print("That's not a valid letter.")

    if lives == 0:
        print(f"Sorry, You died 😞, the word was {word}")
        print(lives_visual_dict[lives])
    else:
        print(f"Yay 😊👏, you guessed the word {word} correctly!")


hangman()
