class Bird:
    def __init__(self,name):
        self.name = name
        
    def fly(self):
        return f'{self.name} is flying....'
        
class Mammal:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        return f'{self.name} is running....'
    
class Bat(Bird, Mammal):
    def __init__(self, name):
        super().__init__(name)
        
bat1 = Bat('Gelco')

print(bat1.fly())
print(bat1.run())