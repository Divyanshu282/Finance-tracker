# 💰 Finance Tracker 🪙

A simple Python-based Personal Finance Tracker to record, edit, and analyze your income and expenses.  
Includes features like monthly summaries, category-based summaries, and the ability to create sample data using Faker.

## 📜 Project Description
To make this project, main code is written in Python. To create and access the dataset, Libraries like pandas and faker are used.

Faker is a very interesting library which can be used to create fake/random data like names, addresses, dates and even a few line sentences.

While making this project, I thought of making a description column to describe the need of the expense made or the describe the source of income briefly. But this being a small personal project, I thought that I should not make this more complicated.

New changes and feature might be added if there is any need for it.

## ✨ Features
- ➕ Add, edit, and delete transactions
- 📊 View income and expense summary
- 🧪 Generate fake transaction data for testing
- 📂 Store data in CSV format for easy portability

## 🛠️ Technologies Used
- 🐍 Python 3.x 
- 🐼 Pandas
- 🤖 Faker

## 📂 Project Files
- `Financial_tracker.py` → Main code to run the finance tracker
- `Dataset_for_FinTracker.py` → Script to create fake transactions for testing
- `data.csv` → Example transaction data file

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Divyanshu282/Finance-tracker.git
2. Navigate into the Folder:
   ```bash
    cd Finance-tracker
3. Install Required Libraries:
   ```bash
    pip install pandas 
    pip install faker
4. Run the dataset program to create a fake/random dataset to run your main code on:
   ```bash
    python Dataset_for_FinTracker.py
4. Run the main program:
   ```bash
    python Financial_tracker.py

## 🚀 Future Enhancements
- Add a GUI interface
- Support multiple users
- Export data in PDF format

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

