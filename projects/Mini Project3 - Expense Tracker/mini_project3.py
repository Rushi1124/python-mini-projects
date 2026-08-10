import json
import os 

if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

else:
    expenses = [{
        "item" : "T-shirt",
        "amount" : 200,
        "category" : "Clothing"
    },
    {
        "item" : "Bus",
        "amount" : 50,
        "category" : "Travel"
    }]

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def calculate_summary():
    total = 0
    highest = 0
    highest_item = ""

    for expense in expenses:
    # print(expense["item"], "->", expense["amount"])
        total += expense["amount"]
        if expense["amount"] > highest:
            highest = expense["amount"]
            highest_item = expense["item"]
    print(f"Total spending: {total}")
    print(f"Highest expense: {highest_item} -> {highest}")


def add_expense():
    item = input("Enter an item:")
    try:
        amount = int(input("Enter amount:"))
        if amount <= 0:
            raise ValueError("Amount should be greater than 0.")
    except ValueError as e:
        print(e)
        return
    category = input("Enter category:")
   
    new_expense = {"item" : item, "amount" : amount, "category" : category}
    expenses.append(new_expense)

    with open("expenses.json", "w")as file:
        json.dump(expenses, file, indent=4)
              
# add_expense()

def view_expenses():
    for expense in expenses:
        print(f"{expense['item']} -> {expense['amount']} -> {expense['category']}")

# view_expenses()


while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Summary")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice:"))
        if choice <= 0 or choice > 4:
            raise ValueError("Choices are given above. Choose from them.")
    except ValueError as e:
        print(e) 
        continue 

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        calculate_summary()

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
