class mammal:
    def walk(self):
        print("walk")



class Dog(mammal):
    def bark(self):
        print("bark")


class Cat(mammal):
    def meow(self):
        print("meow")

dog1= Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.meow
cat1.walk
