# CodeAlpha Basic Chatbot

## 📌 Project Overview

This project is a simple **rule-based chatbot** developed in Python as part of the **CodeAlpha Python Programming Internship**.

The chatbot interacts with the user through the console and provides predefined responses based on the user's input.

It uses basic Python concepts such as `if-elif-else`, functions, loops, strings, and input/output.

---

## 🎯 Objective

The main objective of this project is to build a basic chatbot that can:

* Accept messages from the user.
* Recognize predefined messages.
* Provide appropriate predefined responses.
* Continue the conversation until the user types `bye`.

---

## ✨ Features

* Simple text-based conversation.
* Recognizes greetings such as `hello` and `hi`.
* Responds to `"how are you"`.
* Provides information about the chatbot.
* Responds to unknown messages.
* Allows the user to exit by typing `bye`.
* Uses a simple rule-based approach.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Interface:** Command Line / Console
* **Libraries:** No external libraries required

---

## 📂 Project Structure

```text
CodeAlpha_BasicChatbot/
│
├── chatbot.py
└── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python installation using:

```bash
python --version
```

### Step 2: Open the Project Folder

Open Command Prompt or Terminal inside the project folder.

### Step 3: Run the Program

Execute the following command:

```bash
python chatbot.py
```

---

## 💬 Supported Commands

The chatbot can respond to the following inputs:

| User Input          | Chatbot Response                  |
| ------------------- | --------------------------------- |
| `hello`             | Hi! How can I help you?           |
| `hi`                | Hi! How can I help you?           |
| `how are you`       | I'm fine, thanks!                 |
| `what is your name` | I'm a simple Python chatbot.      |
| `what can you do`   | I can respond to simple messages. |
| `bye`               | Goodbye! Have a nice day!         |

For any other input, the chatbot responds:

```text
Sorry, I don't understand that.
```

---

## 🖥️ Example Output

```text
=================================
       BASIC CHATBOT
=================================
Type 'bye' to exit the chatbot.

You: hello
Bot: Hi! How can I help you?

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: I'm a simple Python chatbot.

You: what can you do
Bot: I can respond to simple messages.

You: bye
Bot: Goodbye! Have a nice day!
```

---

## 📚 Key Concepts Used

### 1. If-Else Statements

`if`, `elif`, and `else` are used to check the user's input and select the appropriate response.

### 2. Functions

The `chatbot_response()` function processes the user's message and returns a response.

### 3. While Loop

A `while` loop keeps the chatbot running until the user enters `bye`.

### 4. User Input

The `input()` function is used to receive messages from the user.

### 5. Strings

String methods such as `.lower()` are used to make the chatbot recognize inputs regardless of capitalization.

---

## 🚀 Future Improvements

The chatbot can be improved by adding:

* More predefined questions and answers.
* Natural Language Processing (NLP).
* Voice input and output.
* A graphical user interface (GUI).
* AI-based responses.
* Conversation history.
* Integration with an external API.

---

## 👨‍💻 Internship Details

**Organization:** CodeAlpha
**Domain:** Python Programming
**Task:** Task 4 – Basic Chatbot

---

## 📄 License

This project is created for educational and internship purposes.
