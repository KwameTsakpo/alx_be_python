class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("Farewell I am being destroyed")
        
    
p1 = Person("Godfred", 31)

print(f'My name is : {p1.name}')