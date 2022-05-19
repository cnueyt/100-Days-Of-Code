
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list).lower()

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_letter = input("Guess a letter?\n")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
liste_cw = []
for i in chosen_word:
    liste_cw.append(i)


for i in range(0, len(liste_cw)):
    if liste_cw[i] == guess_letter:
        print("right")
    else:
        print("wrong")




