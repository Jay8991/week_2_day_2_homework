
# Exercise 1
# 1) Build a Shopping Cart
# Should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a list
# 3) User can add or delete items
# 4) User can see current shopping list
# 5) Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

def show_instructions():
    print("""Type 'add' to add items to your shopping list.
Type 'show' to list all the items in your shopping list.
Type 'delete' to delete items in your shopping list.
Type 'quit' to exit the program. """)
    print("*" * 40)

def show_items(shopping_list):
    for i in shopping_list:
        print(i)

def shopping_cart():
    shopping_list = []

    done = False
    while not done:
        print("\n")
        print("*" * 40)
        show_instructions()

        choice = input("What is your choice? Add | Delete | Show | Quit? ").lower()
        if choice == 'add':
            shopping_item = input("Which item do you want to add to your shopping list? ").lower()    
            shopping_list.append(shopping_item)
        elif choice == 'delete':
            delete_item = input("Which item do you want to delete? ").lower()
            shopping_list.remove(delete_item)
        elif choice == 'show':
            show_items(shopping_list)
        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                done = True
                show_items(shopping_list)
            elif confirm == 'n':
                continue