# Ask for the user's name
name = input("Enter your name: ")

# Open the file in append mode (creates the file if it doesn't exist)
with open("names.txt", "a") as file:
    file.write(name + "\n")

print(f"The name '{name}' has been added to names.txt")

# Ask if the user wants to see all names
choice = input("Do you want to see all names? (y/n): ").strip().lower()

if choice == "y":
    print("\n--- List of all names ---")
    with open("names.txt", "r") as file:
        for line in file:
            print(line.strip())
