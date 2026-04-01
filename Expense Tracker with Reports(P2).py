FILE_NAME = "expenses.txt"

# Add expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    
    with open(FILE_NAME, "a") as file:
        file.write(date + "," + category + "," + amount + "," + description + "\n")
    
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()
            
            if not expenses:
                print("No expenses found.")
                return
            
            print("\n--- All Expenses ---")
            for exp in expenses:
                data = exp.strip().split(",")
                print(f"Date: {data[0]}, Category: {data[1]}, Amount: {data[2]}, Desc: {data[3]}")
    
    except FileNotFoundError:
        print("No expense file found.")

# Generate report
def generate_report():
    total = 0
    category_total = {}
    
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                amount = float(data[2])
                category = data[1]
                
                total += amount
                
                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount
        
        print("\n--- Expense Report ---")
        print(f"Total Expense: {total}")
        
        print("\nCategory-wise:")
        for cat in category_total:
            print(f"{cat}: {category_total[cat]}")
    
    except FileNotFoundError:
        print("No data available.")

# Main menu
def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()