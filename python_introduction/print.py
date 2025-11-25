#Print name
def printName(name):
    print(f'welcome, {name}')

printName("Godfred")

# Area of a rectangle
def area(length, height):
    return (f'Area = {length * height}')

print(area(25,26))

#Determining even or odd

def determiner(number):
    if (number % 2 == 0):
        print(f'The number {number} is even')
    else: print(f'The number {number} is odd')

determiner(21)