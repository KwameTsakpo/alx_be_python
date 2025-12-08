class Dog:
    def make_sound(self):
        return 'Dog barks'

class Cat:
    def make_sound(self):
        return 'Cat meows'

class Bird:
    def make_sound(self):
        return 'Bird chirps'
    
def let_them_speak(trigger):
    print(trigger.make_sound())

dog = Dog()
cat = Cat()
bird = Bird()

let_them_speak(dog)
let_them_speak(cat)
let_them_speak(bird)