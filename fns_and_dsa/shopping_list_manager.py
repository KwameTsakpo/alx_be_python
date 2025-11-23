shopping_list = []

def display_menu():
    print("\n\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    
def addItem():
    choice = input("\nPlease provide name of item to add: ")
    shopping_list.append(choice)
    print(f'{choice} added to cart successfully!!!\n\n')

def removeItem():
    choice = input("\nProvide name of item to remove: ")
    
    if choice in shopping_list:
        shopping_list.remove(choice)
        print(f'{choice} removed from cart successfully!!\n\n')
    else:
        print(f'{choice} does not exist in cart')
    
def displayCart():
    if len(shopping_list) == 0:
        print("Your cart is empty")
    else:
        print("Items in Cart")
        for index, item in enumerate(shopping_list, start=1):
            print(f'{index}. {item}')

def main():
    shopping_list = []

    whileCondition = 1
    
    while (whileCondition > 0 and whileCondition <= 4):
        display_menu()
        
        choice = input("Enter your choice: ")
        

        if choice == '1':
            addItem()
            pass
        elif choice == '2':
            removeItem()
            pass
        elif choice == '3':
            displayCart()
            pass
        elif choice == '4':
            print("Goodbye!")
            whileCondition = 0
            break
        else:
            print("Invalid choice. Please try again.")
            whileCondition = 1
            
        

if __name__ == "__main__":
    main()


