from faker import Faker
import pandas as pd
import random

fake = Faker()
categories = ["Food", "Travel", "Shopping", "Rent", "Salary", "Freelance", "Bills", "Entertainment"]
types = ["Income", "Expense"]

data = []
for i in range(50):  # To make 50 random transactions
    trans_type = random.choice(types)
    amount = random.randint(50, 20000)
    if trans_type == "Expense":
        amount = -abs(amount)
    else:
        amount = abs(amount)
    data.append([
        fake.date_this_year(),  # random date in current year
        random.choice(categories),
        amount,
        trans_type
    ])

df = pd.DataFrame(data, columns=["Date", "Category", "Amount", "Type"])
df.to_csv("data.csv", index=False)  
'''Used "index = false" because we don't want labels/indexes that pandas make while creating a dataframe. 
It make an extra column on the left without a name and only labels.'''
print("Dataset created: data.csv")
