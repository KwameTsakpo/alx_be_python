
def addition(num1, num2):
    return(num1 + num2)

def subtraction(num1,num2):
    return(num1 - num2)

def multiplication(num1, num2):
    return(num1 * num2)

def division(num1,num2):
    if num2 == 0:
        return("Sorry division by zero is undefined")
    else: 
        return(num1/num2)

def perform_operation(num1,num2,operation):
    
    if(operation == "add"):
        return(addition(num1,num2))
    
    elif(operation == "subtract"):
        return(subtraction(num1,num2))
    
    elif(operation == "multiply"):
        return(multiplication(num1,num2))
    
    elif(operation == "divide"):
        return(division(num1,num2))
    
    else:
        return("Invalid input Try Again")
