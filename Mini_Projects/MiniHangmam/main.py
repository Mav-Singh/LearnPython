----------------This is fixed version--------------------------------
#import modules
import random

#wordlist
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for element in range(length):
    placeholder += '_'

#join the elements of the list and display it
# the_word = " ".join(spaces)
print(placeholder)
guess = input("Guess a letter: ").lower()



# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""

while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    
for element in chosen_word:
    if element == guess:
        display += element
    else:
        display += "_"
print(display)





-----------------------------------------this is alternative correct code----------------------------------------------------------------------
#import modules
import random

#wordlist
words = ['batman', 'x-men', 'hulk']

#randomly choose a word
chosen_word = random.choice(words)
print(chosen_word)

#placeholder for chosen word
placeholder = ["_"]*len(chosen_word)
print(f"Guess the word: {' '.join(placeholder)}")

#while loop to keep asking the user to keep guessing the word unless the 
while "_" in placeholder:
    guess = input("Please enter a letter to start guessing: ").lower()
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholder[i] = guess
    print(' '.join(placeholder))

print(f"Congratulations! You guessed the word: {chosen_word}")
#improve the upper for loop to keep recording evey guessed word

------------------------------------------Another session of fixing the stuff...................
import random
word = ['bat','pig','ant']
random_word = random.choice(word)
print(random_word)

#add placeholders in a new list
guessed_word = ['_ ']*len(random_word)
print(" ".join(guessed_word))

#asking for a guess from a user 
guess = input("Guess the alphabet to make the entire word")

# replacing the _ with correctly guessed alphabet
for i in range(len(random_word)):
    if random_word[i] == guess:
        guessed_word[i] = guess



