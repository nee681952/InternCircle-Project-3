# Personal Expense Tracker with CSV

## Project Overview

The Personal Expense Tracker is a beginner-level Python application developed as part of the InternCircle Python Programming Internship.

This application helps users record, view, filter, and analyse their daily expenses. It uses CSV file handling to store expense records permanently, allowing users to access their saved information even after restarting the program.

## Features

- Add new daily expenses.
- View all saved expenses.
- Filter expenses by category.
- Filter expenses by month.
- Calculate total spending for each category.
- Display the grand total of all expenses.
- Identify the biggest single expense.
- Store expense records in a CSV file.
- Menu-driven interface.

## Technologies Used

- Python 3.10
- CSV module
- Datetime module
- Collections module
- Visual Studio Code

## Expense Categories

- Food
- Travel
- Study
- Bills
- Fun

## Project Structure

```text
InternCircle_Project3/
│
├── main.py
├── expenses.csv
└── README.md
```

## How to Run the Project

1. Install Python 3.10 or newer.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Select an option from the main menu.

## Main Menu

1. Add Expense
2. View All Expenses
3. Filter Expenses
4. Expense Summary
5. Quit

## Sample CSV Data

The `expenses.csv` file stores records in the following format:

```csv
date,category,description,amount
2026-10-02,Food,Breakfast,60
2026-10-05,Travel,Bus ticket,40
2026-11-02,Food,Dinner,150
```

## Learning Outcomes

- Understanding Python functions and loops.
- Reading and writing CSV files.
- Validating dates and numeric amounts.
- Filtering structured data.
- Calculating category-wise totals.
- Building a menu-driven Python application.

## Author

Neeraj J.

**Internship:** InternCircle Python Programming Internship

**Project:** Project 03 – Personal Expense Tracker with CSV
