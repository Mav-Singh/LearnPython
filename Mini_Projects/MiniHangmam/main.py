
----------------------------Fix the while loop to stop when the results are met----------------
import random
word = ['bat','pig','ant']
random_word = random.choice(word)
print(f"Random Word: {random_word}")
final = None

#add placeholders in a new list
guessed_word = ['_ ']*len(random_word)
print(" ".join(guessed_word))

#keep asking for a guess from a user
while final !=  random_word:
    guess = input("Guess the alphabet to make the entire word: ")

# replacing the _ with correctly guessed alphabet
    for i in range(len(random_word)):
        if random_word[i] == guess:
            guessed_word[i] = guess
    print(" ".join(guessed_word))
    print(f"guessed_word: {guessed_word}")
    final_word = "".join(guessed_word)

#fix the while loop when the value of random + I am checking using f strings to verify where I am wrong
