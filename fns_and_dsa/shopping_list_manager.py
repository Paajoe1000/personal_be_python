def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("choose an option (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the list.")
        elif choice == '2':
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} is not in the list.")
        elif choice == '3':
            if shopping_list:
                print("current shopping list: ")
                print(shopping_list)
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("Exiting the shopping list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        
if __name__ == "_main_":
    main()

