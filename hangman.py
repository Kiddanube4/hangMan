import random
from Hangman_art import logo, stages
# game logo
print(logo)
# import a words.txt
word_file = "E:/pythonProject/words"
words = open(word_file).read().splitlines()
# choose a random word from it
choosen_word = list(random.choice(words))
bar_count = len(choosen_word)
# use for debugging: print(choosen_word)
# printing bars
bars = []
for x in range(0, bar_count):
    bars.append("_")
print(*bars, sep=" ")

blank_size = len(choosen_word)
life_count = len(stages) - 1
# game ending condition
while not life_count == 0 and blank_size != 0:
    # game engine
    guess = input("Guess a letter \n").lower()
    for position in range(bar_count):
        if guess == choosen_word[position]:
           bars.insert(position, guess)
           bars.pop()
           blank_size -= 1

    print(*bars, sep=" ")
    if guess not in choosen_word:
        print(stages[life_count])
        life_count -= 1

if life_count == 0:
    print(stages[life_count])
    print("You loose")
else:
    print("You win")
