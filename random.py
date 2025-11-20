import random



play = "y"

count = 0

while play == "y":
      print(f'Number of tries {count}')

      secret_number = random.randint(1,10)

      guess = int(input("Guess the random number: "))

      match guess :
            case _ if guess == secret_number:
                  print("Congratulations, you guessed it!")
            case _ if guess > secret_number:
                  print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                  print("Nope, your guess is a bit low. Give it another shot!")
      
      play = str(input("play again? Yes or No(y/n)"))
      count += 1

print("Thanks for playing !!!!!!")


