# Read and print all lines from server_names.txt

# Open the file in read mode
with open("server_names.txt", "r") as file:
    # Read all lines
    lines = file.readlines()

# Print each line
for line in lines:
    print(line.strip())  # .strip() removes extra spaces or newlines
