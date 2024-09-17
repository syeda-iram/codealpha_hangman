import random

#create a list of words
word_list = ['UMBRELLA', 'TELEPHONE', 'PLATE', 'CUPBOARD', 'MOBILE', 'ICE', 'PHONE', 'LAPTOP', 'COMPUTER', ]

guesses = 5    #total number of guesses

#computer randomly selects the word to be guessed
chosen_word = random.choice(word_list)

guessed_word = '-' * len(chosen_word)
print(guessed_word)    #display the dashes

while guesses != 0:
    letter = input("Guess a letter: ")    #prompt the user to guess a letter
    letter = letter.upper()    #convert the alphabet to uppercase

#check if letter entered by user is present in the word
    if letter in chosen_word:
        for index in range(len(chosen_word)):
            if letter == chosen_word[index]:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1 :]    #replace letter with hyphen
        print(guessed_word, '\n')

#if the word is completely guessed
        if guessed_word == chosen_word:
            print('\t\t\t CONGRATULATIONS!!!')
            print('\t\t\t YOU WON \n')
            break

#if user guesses wrong letter
    else:    
        guesses -= 1
        print('Wrong Guess!!')
        print(guesses, "guesses left! \n\n")
        
#if number of guesses becomes 0
else:
    print('\t\t\t GAME OVER')
    print('\t\t\t YOU LOSE!!! \n')

#show the correct answer
print('The correct word is', chosen_word)