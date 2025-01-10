# Function for continous display of menu until user inputs exit
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
        choice = input("Enter your choice:")
        if choice == "1":
            item = input("Enter the item to add:").strip()
            if item:
                shopping_list.append(item)
            else:
                print("No item was entered. Try again")
        elif choice == "2":
            item = input("Enter the item to remove from shopping list:").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("The item entered is not in list.")
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice. Try again")
        break
if __name__ == "__main__":
    main()