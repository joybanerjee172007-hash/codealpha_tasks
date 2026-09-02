import random

# List of 5 predefined words
words = ["python", "computer", "program", "keyboard", "internet"]

# Select a random word
word = random.choice(words)

# Variables
guessed_word = ["_"] * len(word)
incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("=================================")
print("       WELCOME TO HANGMAN")
print("=================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabetic letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("Correct guess!\n")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")


# Game result
if "_" not in guessed_word:
    print("=================================")
    print("          YOU WON! 🎉")
    print("=================================")
    print("The word was:", word)
else:
    print("=================================")
    print("          GAME OVER!")
    print("=================================")
    print("The correct word was:", word)
