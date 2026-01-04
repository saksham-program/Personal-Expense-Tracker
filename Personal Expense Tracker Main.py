expenses = []   

def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        note = input("Enter note: ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")

    elif choice == "3":
        print("Exiting program. Goodbye")
        break

    else:
        print("Invalid choice. Please try again.")


