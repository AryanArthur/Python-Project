# Hangman Project
import random
word_list = ["Computer", "Balloon", "Honesty", "Goodness", "Laptop"] #Project Hangman
random_word = random.choice(word_list)
blank_list = ["_"]*len(random_word)
print(blank_list)

lives = 5
while "_" in blank_list and lives > 0:
    guess_a_letter = input("guess a letter").lower()
    if len(guess_a_letter) >= 2:
        print("game over. you entered more than one letter!")
        break

    for i in range(len(random_word)):
        if random_word[i].lower() == guess_a_letter:
            blank_list[i] = guess_a_letter

    if guess_a_letter not in random_word.lower():
        lives -= 1
        print(f"Wrong guess. lives left: {lives}")
    print(blank_list)

if "_" not in blank_list:
    print("You won!")
elif lives == 0:
    print("game over")
