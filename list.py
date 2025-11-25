import random

#Random number exercise

randomList = []

for _ in range(10):
    randomList.append(random.randint(1, 10))
    
print(randomList)

print(set(randomList))

#list
fruits = ["apple","orange","pineapple","Guava","Melon"]

print(fruits[1])


#Dictionaries
book = {"author":"Fred Godlings","title":"The lost Species","genre":"Sci-Fiction"}

print(book["genre"])

#print number of items in dict
print(len(book))