class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f'{self.name} is eating')
    
    def sleep(self):
        print(f'{self.name} is sleeping now')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

dog1 = Dog('Bruno')

dog2 = Animal('Lion')
   
   
print("Dog 1 details: \n")        
dog1.eat()
dog1.sleep()     
        
print("Dog 2 details: \n")        
dog2.eat()
dog2.sleep()

