#a class is blue print of an object. guides on how an object should look like
# objects are instances of a class.act as a prototype
class Person:
    name = "Joe"
    age = 45
    gender = "male"
    def walk(self):
        print("walking")

p = Person()
p.walk()
print(p.name)
