# Define the number of rows
rows = 5

# Use a loop to print the stars in a sequence
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print("")
