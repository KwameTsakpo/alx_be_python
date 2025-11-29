class Product:
    
    stock = []
    
    def __init__ (self):
        pass
    
    def addProduct(self):
        name = input('Please enter name of product: ')
        price = float(input('Price of the product: '))
        quantity = int(input('Product Quantity: '))
        
        self.stock.append({
            "name": name,
            "price": price,
            "quantity": quantity 
        })
        
        print(f'{name} added to stock successfully')
        
    def displayProducts(self):
        for index, item in enumerate(self.stock):
            print(f'----------------------\n Product id: {index}\n Name: {item["name"]} \n Price: {item["price"]}\n Quantity:  {item["quantity"]}\n------------------------- ')
    
    def totalOfProducts(self):
        total = 0
        for item in self.stock:
            total += item["price"] * item["quantity"]
        
        self.displayProducts()
        
        print(f'-----------------\n Total Cost of items is: {total}GHC')
    
    
    
product = Product()


user_choice = 0

while user_choice != 4:
    print("Welcome to Your Product Management System")
    print("1. Add Product")
    print("2. Display Product")
    print("3. Calculate Total of products in stock")
    print("4. Exit")
    
    user_choice = int(input("Please enter an option: "))

    match user_choice:
        case 1:
            product.addProduct()
        case 2:
            product.displayProducts()
        case 3:
            product.totalOfProducts()
        case 4:
            print("Thank you for shopping with us")
            break
        case _:
            print("Invalid input. Please try again.")


    
    