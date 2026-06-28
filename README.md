# CodeAlpha: Stock Portfolio Tracker (Task 2)

A command-line terminal application that calculates financial valuations of stock positions based on manual user inputs and hardcoded market evaluation data. This project was developed as part of the CodeAlpha Python Programming Internship.

## 🚀 Features
- **Dynamic Inventory Management**: Allows users to dynamically input stock symbols and asset quantities to assemble custom portfolios.
- **Interactive Validation**: Verifies inputs against an existing internal database dictionary and checks for invalid share inputs.
- **Financial Computations**: Automatically tabulates individual asset holding totals alongside comprehensive portfolio values.
- **CSV Data Exports**: Prompts users to automatically save summaries directly into clean local `.csv` sheet layouts for later use.

## 🛠️ Key Concepts Used
- Dictionaries mapping asset tickets to values.
- Input validation strings and `try-except` execution loops.
- Arithmetic formula processing.
- Persistent local File I/O (`with open()`).

## 📦 How to Run
1. Ensure you have Python 3 installed on your machine.
2. Open your terminal, navigate to the folder, and run:
   ```bash
   python portfolio_tracker.py
   ```
