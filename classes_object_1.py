class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

person1 = Student("Godfred", 36)
person2 = Student("Kwame", 50)

print(f'your name is {person1.getName()} and you are {person1.getAge()} years old')
print(f'your name is {person2.getName()} and you are {person2.getAge()} years old')