# Job Role Classification without libraries

# Predefined roles with keywords
roles = {
    "Data Scientist": ["machine learning", "data", "python", "analysis", "model"],
    "Web Developer": ["html", "css", "javascript", "react", "website"],
    "Database Administrator": ["sql", "database", "mysql", "oracle", "queries"],
    "Mobile Developer": ["android", "ios", "mobile", "flutter", "app"],
    "Business Analyst": ["business", "reports", "analysis", "excel", "data"]
}

# Function to classify job role
def classify_role(description):
    description = description.lower()
    score = {}

    # Count keyword matches
    for role in roles:
        score[role] = 0
        for keyword in roles[role]:
            if keyword in description:
                score[role] += 1

    # Find role with highest score
    best_role = None
    max_score = 0

    for role in score:
        if score[role] > max_score:
            max_score = score[role]
            best_role = role

    return best_role if max_score > 0 else "Role not identified"

# Main program
def main():
    print("=== Online Job Role Classification ===")

    while True:
        text = input("\nEnter job description (or type 'exit'): ")

        if text.lower() == "exit":
            print("Exiting...")
            break

        result = classify_role(text)
        print("🎯 Predicted Role:", result)

# Run program
if __name__ == "__main__":
    main()