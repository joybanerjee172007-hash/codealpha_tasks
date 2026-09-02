# CodeAlpha Hangman Game

## 📌 Project Overview

This project is a simple **text-based Hangman Game** developed in Python as part of the **CodeAlpha Python Programming Internship**.

The player has to guess a randomly selected word one letter at a time. The player is allowed a maximum of **6 incorrect guesses**. The game continues until the player correctly guesses the complete word or uses all six incorrect attempts.

## 🎯 Objective

The objective of this project is to practice basic Python programming concepts such as:

* Variables
* Lists
* Strings
* `while` loops
* `if-else` statements
* User input
* The `random` module
* Basic input validation

## 🎮 Features

* Contains 5 predefined words.
* Randomly selects one word for each game.
* Allows the player to guess one letter at a time.
* Displays correctly guessed letters.
* Keeps track of previously guessed letters.
* Allows a maximum of 6 incorrect guesses.
* Displays the result when the game ends.
* Prevents repeated letter guesses.
* Validates user input.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Module:** `random`
* **Interface:** Command Line / Console

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Download or Clone the Repository

Clone the GitHub repository or download the project files.

### Step 3: Open the Project Folder

Open the terminal or command prompt inside the project folder.

### Step 4: Run the Program

Use:

```bash
python hangman.py
```

## 🕹️ How to Play

1. The program randomly selects a word from the predefined word list.
2. The selected word is displayed as underscores.
3. Enter one letter at a time.
4. If the letter exists in the word, it will be revealed.
5. If the letter is incorrect, one attempt will be deducted.
6. The player can make a maximum of 6 incorrect guesses.
7. The player wins if all letters are guessed correctly.
8. The player loses if all 6 incorrect attempts are used.

## 📋 Example

```text
=================================
       WELCOME TO HANGMAN
=================================
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Guessed letters:
Incorrect guesses left: 6

Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses left: 6
```

## 📚 Concepts Used

### Random Module

The `random.choice()` function is used to select a random word from the predefined list.

```python
word = random.choice(words)
```

### While Loop

The `while` loop keeps the game running until the player wins or loses.

### Lists

Lists are used to store:

* Predefined words
* Guessed letters
* The currently revealed word

### Conditional Statements

`if-else` statements are used to determine whether the player's guess is correct or incorrect.

### Strings

Strings are used for storing and processing words and user input.

## 🚀 Future Improvements

The project can be improved by adding:

* Different difficulty levels
* More words
* Categories such as animals, countries, movies, etc.
* A scoring system
* A graphical user interface
* A hangman drawing using ASCII art
* A word database or external API

## 👨‍💻 Internship Task

**Organization:** CodeAlpha
**Domain:** Python Programming
**Task:** Task 1 – Hangman Game

## 📄 License

This project is created for educational and internship purposes.
