# Write your code here
import random


def show_result():
    print(''.join([letter for letter in tobe_showed_string]))


# Write your code here
print("H A N G M A N\n")
list_of_words = ['python', 'java', 'kotlin', 'javascript']

word = random.choice(list_of_words)

word_letters_set = set(word)

number_of_rights = 8

guessed_letters_set = set()

true_guessed_letters_set = set()

tobe_showed_string = list("-" * len(word))

show_result()
# print(''.join([letter for letter in tobe_showed_string]))

while True:
    play_or_exit = input(f'Type "play" to play the game, "exit" to quit: ')

    if play_or_exit == "exit":
        break
    elif play_or_exit != "play":
        continue

    while number_of_rights > 0:

        guessed_letter = input(f"Input a letter: ")

        if len(guessed_letter) > 1:
            print("You should input a single letter\n")
            show_result()
            continue

        if not guessed_letter.islower():
            print("Please enter a lowercase English letter\n")
            show_result()
            continue

        if guessed_letter in guessed_letters_set:
            print("You've already guessed this letter\n")
            show_result()
            continue

        guessed_letters_set.add(guessed_letter)

        if guessed_letter in word_letters_set:
            for index in range(len(word)):
                if guessed_letter == word[index]:
                    true_guessed_letters_set.add(guessed_letter)
                    tobe_showed_string[index] = guessed_letter
        else:
            print("That letter doesn't appear in the word")
            number_of_rights -= 1

        # print(attempts)

        if true_guessed_letters_set == word_letters_set or number_of_rights == 0:
            break
        else:
            print()
            show_result()
            # print(''.join([letter for letter in tobe_showed_string]))

    if number_of_rights > 0:
        print("You guessed the word " + word + "!")
        print("You survived!")
    else:
        print("You lost!")
