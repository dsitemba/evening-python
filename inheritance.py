# parent class, you need a parent and a child
class Animal:
    def speak(self):
        print("Animal is speaking")

#child class
class Dog (Animal): # parent class after the child name/inheritance
    def bark(self):
        print("Dog is barking")

class cat (Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.speak()

c= cat()
c.meow()
