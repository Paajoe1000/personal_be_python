number = int(input("Enter a number to see its multiplication table: "))
current_number = range(1,11)
for y in current_number:
    z = number * y
    print(number, "*", y, "=", z )