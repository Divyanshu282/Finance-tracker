import pandas as pd
from datetime import datetime

FILE = '/Users/divyanshusingh/Documents/Python Projects/Projects/data.csv'

def load_data():
    try:
        return pd.read_csv(FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])

def save_data(df):
    df.to_csv(FILE, index=False)

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    txn_type = input("Type (Income/Expense): ").capitalize()

    if txn_type == "Expense":
        amount = -abs(amount)
    elif txn_type == "Income":
        amount = abs(amount)

    new_row = pd.DataFrame([[date, category, amount, txn_type]],
                           columns=["Date", "Category", "Amount", "Type"])
    df = load_data()
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    print("Transaction added!")

def show_summary():
    df = load_data()
    if df.empty:
        print("No transactions found.")
        return
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expense = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = income + expense
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{abs(expense)}")
    print(f"Current Balance: ₹{balance}")

def show_all_transactions():
    df = load_data()
    if df.empty:
        print("No transactions yet.")
    else:
        print(df)

def delete_transaction():
    df = load_data()
    print(df)
    idx = int(input("Enter the index of the transaction to delete: "))
    if idx in df.index:
        df = df.drop(idx)
        save_data(df)
        print("Transaction deleted.")
    else:
        print("Invalid index.")
    return df

def edit_transaction():
    df = load_data()
    print(df)
    idx = int(input("Enter the index of the transaction you want to edit: "))
    
    if idx in df.index:
        print("Leave a field empty if you dont want to change it.")
        new_date = input(f"New date (YYYY-MM-DD) [{df.at[idx, 'Date']}]: ")
        new_amount = input(f"New amount [{df.at[idx, 'Amount']}]: ")
        new_category = input(f"New category [{df.at[idx, 'Category']}]: ")
        

        if new_date.strip():
            df.at[idx, 'Date'] = new_date
        if new_amount.strip():
            df.at[idx, 'Amount'] = float(new_amount)
        if new_category.strip():
            df.at[idx, 'Category'] = new_category
        
        save_data(df)
        print("Transaction updated.")
    else:
        print("Invalid index.")
    
    return df


def menu():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Show Summary")
        print("4. Delete Transaction")
        print("5. Edit Transaction")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_all_transactions()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            edit_transaction ()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

menu()
