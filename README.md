<h1 align="center">🌟 Logic Box 🌟</h1>
<h3 align="center">🐍 Menu-Driven Python Program for Patterns & Number Analysis 💻</h3>

<p align="center">
  <b>A beginner-friendly Python project that lets the user generate star patterns, analyze numbers as odd/even, and calculate their sum through a simple menu-driven system ✨</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Project-Beginner%20Friendly-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Menu%20Driven-orange?style=for-the-badge" />
</p>

---

# 📖 Project Overview
**Logic Box** is a simple **menu-driven Python project** designed for beginners to practice loops, conditions, pattern printing, and number analysis.

The program shows a menu with 3 options:
1. **Generate Pattern** ⭐  
2. **Analyze Numbers** 🔢  
3. **Exit** 🚪  

Depending on the user’s choice, the program can:
- print a star (`*`) pattern row by row
- check whether numbers in a range are **odd or even**
- calculate the **sum** of numbers in that range
- exit the program when the user selects option 3

---

# ✨ Features
✔️ Menu-driven Python program  
✔️ Generates star pattern using nested loops  
✔️ Checks whether numbers are **Odd** or **Even**  
✔️ Calculates the **sum** of numbers in a given range  
✔️ Uses `while True` loop for repeated menu display  
✔️ Uses `match-case` for handling user choices  
✔️ Great beginner project for logic building  

---

# 🛠️ Tech Stack
| Technology | Purpose |
|-----------|---------|
| **Python 3** | Programming Language |
| **IDLE / VS Code / PyCharm** | To run the program |

---

# 📂 Project Structure
```bash
Logic-Box/
│── logic box.py
│── README.md
│── screenshot.png
```

---

# 📸 Output Screenshot
<p align="center">
  <img src="image(28).png" alt="Logic Box Output" width="900">
</p>

---

# 💻 Source Code
```python
# Student Data Organizer
# Menu-Driven Program

while True:
    print("\n1. Generate Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            rows = int(input("Enter number of rows: "))
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()

        case 2:
            start = int(input("Enter start number: "))
            end = int(input("Enter end number: "))
            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(num, "is Even")
                else:
                    print(num, "is Odd")

                total += num

            print("Sum =", total)

        case 3:
            print("Goodbye!")
            break

        case _:
            print("Invalid Choice")
```

---

# ▶️ How to Run the Project
## Step 1: Save the Python file
Save your program with a file name like:

```bash
logic box.py
```

## Step 2: Open in Python IDE
You can run it in:
- **Python IDLE**
- **VS Code**
- **PyCharm**

## Step 3: Run the Program
Execute the file. The menu will appear on the screen.

## Step 4: Choose an Option
You can choose:
- **1** → to generate star pattern
- **2** → to analyze numbers and find sum
- **3** → to exit the program

---

# 📚 Concepts Used
- `while True`
- `match-case`
- nested `for` loops
- `if-else`
- arithmetic operations
- range-based iteration
- menu-driven programming

---

# 🎯 Learning Objectives
By making this project, you can practice:
- creating a **menu-driven program**
- using **loops inside loops**
- checking **odd/even logic**
- calculating sum using loops
- taking user input
- using **match-case** for decision making

---

# 📝 Sample Output
```bash
1. Generate Pattern
2. Analyze Numbers
3. Exit
Enter your choice: 1
Enter number of rows: 5
*
**
***
****
*****

1. Generate Pattern
2. Analyze Numbers
3. Exit
Enter your choice: 2
Enter start number: 1
Enter end number: 10
1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd
6 is Even
7 is Odd
8 is Even
9 is Odd
10 is Even
Sum = 55

1. Generate Pattern
2. Analyze Numbers
3. Exit
Enter your choice: 3
Goodbye!
```

---

# 🚀 Why this project is useful
This project is a great beginner exercise because it combines:
- **pattern printing**
- **number analysis**
- **looping logic**
- **conditional statements**
- **menu-driven structure**

It helps in building strong logic for future Python projects 💡

---

# 💖 Author Note
Made with dedication for **Python practice, problem solving, and logic building** 🌸✨

---

<p align="center">
  ⭐ If you like this project, don't forget to give it a star on GitHub ⭐
</p>
