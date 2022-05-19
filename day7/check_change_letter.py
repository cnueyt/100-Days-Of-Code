import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list).lower()

cw=[]
for letter in chosen_word:
    cw.append(letter)
    
liste = []

for i in range(0,len(chosen_word)):
        liste.append("_")

end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a letter?\n")
    
    for i in range (0, len(chosen_word)):
        if chosen_word[i] == guess_letter:
                liste[i] = guess_letter
    print(liste)

    if "_" not in liste:
        end_of_game = True
        print("you won")
 

  








