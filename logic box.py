# Student Data Organizer
# Menu-Driven Program

print("1. Generate Pattern")
print("2. Analyze Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

match choice:
        case 1:
                rows = int(input("Enter number of rows: "))
                for i in range(1, rows + 1):
                 for j in range(i):
                        print("*", end="")
                 print()
        case 2:
                start = int(input("Enter start number: "))
                end = int(input("Enter end number: "))
                total = 0
                for num in range(start, end + 1):
                        if num % 2 == 0:
                                print(num, "is Even")
                        else:
                                print(num, "is Odd")

                        total += num

                print("Sum =", total)
        case 3:
                print("Goodbye!")
        case"_":
                print("Invalid Choice")

