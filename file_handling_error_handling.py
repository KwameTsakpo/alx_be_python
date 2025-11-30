import os;


def createFile():
    fileName = input('\nPlease enter file name: ')
    fileText = input('\nPlease enter text to insert in file: ')
    while True:
        try:
           with open(fileName, 'x') as file:
               print(f'\n{fileName} created successfully!!!\n')
               file.write(fileText)
               break
        except Exception as e:
            print(f'\n{e}: Sorry file already exist')

def readFile():
    fileName = input('\nPlease enter file name to read:')

    while True:
        try:
            with open(fileName, 'rt') as file:
                print(file.read())
                print('\n_________________________\nfile information pasted\n_________________________')
                break
        except FileNotFoundError:
            print('Sorry file not found')

def writeToFile():
    while True:
        try:
            fileName = input('Please provide file name to write to: ')
            fileText = input('Please provide text to add to file: ')
            with open(fileName, 'a') as file:
                file.write(f'\n\n{fileText}')
                print(f'{fileText} successfully written to {fileName}')
            break
        except:
            print('Sorry something went wrong')

def deleteFile():
    fileName = input('Please enter file name to remove: ')
    
    if os.path.exists(fileName):
        os.remove(fileName)
        print(f'{fileName} successfully removed!!')
    else:
        print("Sorry file doesn't exist")

userChoice = 0

while userChoice != 4:
    print('\n\nWelcome to my File Handling Exercise\n------------------------------------\n')
    print('1. Create file')
    print('2. Read file')
    print('3. Add text to file')
    print('4. Delete file')
    print('5. exit')

    while True:
        try:
            userChoice = int(input('Please Enter your choice: '))
            break
        except ValueError:
            print('\nInvalid Error. Please Try again\n')

    match userChoice:
        case 1:
            createFile()
        case 2:
            readFile()
        case 3:
            writeToFile()
        case 4:
            deleteFile()
        case 5:
            print('\nThank you for trying us out. Byes!!!!!!!')
        case _:
            print('Invalid Input please try again')