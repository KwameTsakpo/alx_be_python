class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate(self):
        return (f'Width: {self.width}\nHeight: {self.height}')

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width,height)
    
    def calculate(self):
        return self.width * self.height
    

rect1 = Rectangle(20,10)

shape1 = Shape(40,50)

print(shape1.calculate())
print(rect1.calculate())
    