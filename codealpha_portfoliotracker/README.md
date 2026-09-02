# 📈 Stock Portfolio Tracker

## 📌 Project Overview

The **Stock Portfolio Tracker** is a simple Python-based program that allows users to track their stock investments. The user enters the stock name and quantity, while the program uses predefined stock prices to calculate the total investment value.

The program also provides an option to save the portfolio details into a `.txt` file.

---

## 🎯 Objective

The main objective of this project is to create a simple stock tracking system using:

* Python dictionaries
* User input and output
* Loops and conditional statements
* Basic arithmetic operations
* File handling

---

## ✨ Features

* Display available stocks and their prices
* Accept stock names from the user
* Accept the quantity of stocks
* Calculate investment value for each stock
* Calculate total investment
* Display a portfolio summary
* Optionally save the portfolio to a text file

---

## 💻 Technologies Used

* **Programming Language:** Python
* **Data Structure:** Dictionary
* **File Format:** `.txt`

---

## 📊 Predefined Stock Prices

The program contains a hardcoded dictionary:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}
```

> **Note:** These are manually defined example prices and are not live market prices.

---

## ⚙️ How It Works

1. The program displays the available stocks.
2. The user enters the number of different stocks.
3. The user enters the stock name.
4. The user enters the quantity.
5. The program checks whether the stock exists.
6. The investment value is calculated using:

```text
Investment = Stock Price × Quantity
```

7. The program calculates the total investment.
8. The portfolio summary is displayed.
9. The user can optionally save the result in `portfolio.txt`.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Save the Program

Save the Python program as:

```text
stock_portfolio.py
```

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python stock_portfolio.py
```

---

## 🧪 Example

### Input

```text
Enter the number of stocks you want to buy: 2

Enter stock name 1: AAPL
Enter quantity of AAPL: 5

Enter stock name 2: TSLA
Enter quantity of TSLA: 2
```

### Output

```text
AAPL Investment: $900
TSLA Investment: $500

===== PORTFOLIO SUMMARY =====
AAPL | Quantity: 5 | Price: $180 | Value: $900
TSLA | Quantity: 2 | Price: $250 | Value: $500

Total Investment: $1400
```

---

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio.py
├── portfolio.txt
└── README.md
```

`portfolio.txt` is created only when the user chooses to save the portfolio.

---

## 📚 Key Concepts Learned

* Dictionary
* `for` loop
* `if-else`
* User input
* String methods
* Arithmetic operations
* File handling
* Formatted output

---

## 🚀 Future Improvements

The project can be improved by adding:

* Live stock prices using an API
* Buy and sell transactions
* Profit/loss calculation
* Multiple users
* CSV file storage
* Graphical user interface (GUI)
* Portfolio performance charts

---

## 👨‍💻 Author

**Joy Banerjee**

---

## 📄 License

This project is created for **educational and college project purposes**.
