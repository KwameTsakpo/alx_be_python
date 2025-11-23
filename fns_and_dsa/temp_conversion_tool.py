FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return(FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit-32))


def convert_to_fahrenheit(celsius):
    return((CELSIUS_TO_FAHRENHEIT_FACTOR * celsius)+32)

def main():
    temp = int(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
    if unit == 'C':
        if temp:
            print(f'{temp}°C is {convert_to_fahrenheit(temp)}°F')
    elif unit == 'F':
        if temp:
            print(f'{temp}°F is {convert_to_celsius(temp)}°C')
    else:
        print('Please enter valid temperature')
                
main()
