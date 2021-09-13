import random

import time

import images

correctly_guessed_letters = []

incorrectly_guessed_letters = []


def intro():
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")


time.sleep(2)


def welcome():

    name = input("""
==============================================
> Welcome to the HangYou Game ! Please enter your nickname: <""").capitalize()

    time.sleep(2)

    if name.isalpha() == True:
        print("""
>>> Hi""", name, """glad to hang you here! <<< 
    
The computer will randomly choose a word and you will try to guess it.
But you will fail!""")
        time.sleep(1)
        print("""================================================================""")
        time.sleep(1)

        print("""Hang in there!
        
        """)

    else:
        print('Please enter your nickname using letters only')
        name = input('Enter a game name here: ')
        time.sleep(1)
        print('Hi!', name, 'Follow the rules, they say!')


def choose_level():

    level_mode = input(

        "Enter level mode""\n""E for Easy""\n""H for Hard""\n").upper()

    if level_mode == "E":

        lives_left = 6

        # print(images.HANGMAN[6 - lives_left])

    else:

        lives_left = 3

        # print(images.HANGMAN[3 - lives_left])

    return [level_mode, lives_left]


def get_word(level_mode):

    taken_words = []

    with open('countries-and-capitals.txt', 'r') as f:

        for line in f:
            word_taken = line.split(" | ")

            if level_mode == "E":

                taken_words.append(word_taken[0])
            else:
                taken_words.append(word_taken[1])

    choosen_word = random.choice(taken_words)

    print(choosen_word)

    return choosen_word


def draw_word(choosen_word):

    secret_word = ''

    for i in range(0, len(choosen_word)):

        if choosen_word[i].lower() == " ":

            secret_word += " "

        elif choosen_word[i].lower() in correctly_guessed_letters:

            secret_word += choosen_word[i].lower()

        else:

            secret_word += "_"

    return secret_word.capitalize()


def get_one_valid_letter(choosen_word, lives_left):
    # Will make sure the user types only 1 letter that has not been used before

    is_letter_valid = False

    while is_letter_valid is False:

        letter = input("Enter guess letter: ")

        letter = letter.strip().lower()

        if len(letter) != 1:

            print("Letter must be of length 1")

        elif letter.isalpha():

            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:

                print("You have already used the letter " +
                      letter + ", please try again")
            else:
                add_letter_to_correct_or_incorrect_list(
                    letter, choosen_word, lives_left)

                is_letter_valid = True
        else:
            print("Letter must be (a-z)")

    return letter


def is_correct_letter(letter, choosen_word):

    if letter in choosen_word:

        return True

    else:

        return False


def add_letter_to_correct_or_incorrect_list(letter, choosen_word, lives_left):

    if is_correct_letter(letter, choosen_word) is True:

        correctly_guessed_letters.append(letter)

        return correctly_guessed_letters

    else:

        lives_left -= 1

        incorrectly_guessed_letters.append(letter)

        return incorrectly_guessed_letters


def game_over(choosen_word):

    print(f"this is {choosen_word} right word")

    quit()


def hangman_drawing():

    pass


def main():

    intro()

    welcome()

    [level_mode, lives_left] = choose_level()

    choosen_word = get_word(level_mode)

    print(draw_word(choosen_word))

    while draw_word(choosen_word) != choosen_word:

        if lives_left > 0:

            get_one_valid_letter(choosen_word, lives_left)

            print(draw_word(choosen_word))

        else:

            print("You lost bit ch!")

            game_over()

    print("You lucky bastard!")

    game_over()


if __name__ == '__main__':

    main()
