pattern = int(input("Enter the size of the pattern: "))
rows = 4
for i in range(rows):
    for j in range(i):
        print("*", end="")
        print("")