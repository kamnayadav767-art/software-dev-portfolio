import json
import os

FILE_NAME = "bugs.json"

# Load existing bugs
def load_bugs():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save bugs to file
def save_bugs(bugs):
    with open(FILE_NAME, "w") as file:
        json.dump(bugs, file, indent=4)

# Add new bug
def add_bug():
    bugs = load_bugs()
    bug = {
        "id": len(bugs) + 1,
        "title": input("Enter bug title: "),
        "description": input("Enter description: "),
        "priority": input("Enter priority (Low/Medium/High): "),
        "status": "Open"
    }
    bugs.append(bug)
    save_bugs(bugs)
    print("✅ Bug added successfully!")

# View bugs
def view_bugs():
    bugs = load_bugs()
    if not bugs:
        print("No bugs found.")
        return
    for bug in bugs:
        print(f"\nID: {bug['id']}")
        print(f"Title: {bug['title']}")
        print(f"Description: {bug['description']}")
        print(f"Priority: {bug['priority']}")
        print(f"Status: {bug['status']}")

# Update bug status
def update_bug():
    bugs = load_bugs()
    bug_id = int(input("Enter Bug ID to update: "))
    
    for bug in bugs:
        if bug["id"] == bug_id:
            print("Current Status:", bug["status"])
            bug["status"] = input("Enter new status (Open/Closed): ")
            save_bugs(bugs)
            print("✅ Bug updated!")
            return
    
    print("❌ Bug not found.")

# Delete bug
def delete_bug():
    bugs = load_bugs()
    bug_id = int(input("Enter Bug ID to delete: "))
    
    bugs = [bug for bug in bugs if bug["id"] != bug_id]
    save_bugs(bugs)
    print("🗑 Bug deleted!")

# Main menu
def main():
    while True:
        print("\n--- Bug Tracking System ---")
        print("1. Add Bug")
        print("2. View Bugs")
        print("3. Update Bug")
        print("4. Delete Bug")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_bug()
        elif choice == "2":
            view_bugs()
        elif choice == "3":
            update_bug()
        elif choice == "4":
            delete_bug()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()