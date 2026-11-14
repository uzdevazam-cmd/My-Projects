print("Welcome to the Daily Expense Tracker!")
print()
print('Menu:')
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    menu = input()
    counter = 0

    if int(menu) < 1 or int(menu) > 5:
        print("Invalid choice. Please try again.")
    else:
        if menu == '5':
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        elif menu == '1':
            expense = float(input())
            expenses.append(expense)
            print("Expense added successfully!")
        elif menu == '2':
            if expenses == []:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for i, v in enumerate(expenses):
                    print(f"{i + 1}. {v}")
        elif menu == '3':
            if expenses == []:
                print("No expenses recorded yet.")
            else:
                for i in expenses:
                    counter += i
                print(f"Total expense: {counter}")
                print(f"Average expense: {counter / len(expenses)}")
        elif menu == '4':
            if expenses == []:
                print("No expenses recorded yet.")
            else:
                expenses = []
                print("All expenses cleared.")
