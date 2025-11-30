class ValueTooHigh(Exception):
        pass

def maxNumberChecker(number):
    if number > 100:
        raise ValueTooHigh("Sorry Number is greater than 100")
    else: 
        print("Your number is ",number)




maxNumberChecker(1)