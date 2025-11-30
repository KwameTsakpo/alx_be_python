def sum():
    while True:
        try:
            num1 = float(input("Please input first number: "))
            num2 = float(input("Please input second number: "))
            results = num1/num2
            break
        except ZeroDivisionError:
            print("Division by zero is not allowed, Please try again")
        
        
    print(f'Result of {num1}/{num2} = {results}')

sum()