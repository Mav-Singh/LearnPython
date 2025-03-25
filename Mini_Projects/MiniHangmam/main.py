
#Import Modules
import random

#Create a list of words
word = ['bat','pig','ant']

#randomly choose a word from the list 
random_word = random.choice(word)

#Variables for later use
final_word = None

#add placeholders to Guessed word based on the length of the random word
guessed_word = ['_ ']*len(random_word)
print(" ".join(guessed_word))

#keep asking for a guess from a user
while final_word!=  random_word:
    guess = input("Guess the alphabet to make the entire word: ")

# replacing the _ with correctly guessed alphabet
    for i in range(len(random_word)):
        if random_word[i] == guess:
            guessed_word[i] = guess
    print(" ".join(guessed_word))
    final_word = "".join(guessed_word)
print("Congratulations you guessed the word right")

#Next things to do: make this program as required in 100 days of python program
