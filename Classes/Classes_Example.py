class Person:
    def __init__(self, name):
        self.name = name

        pass

    def talk(self):
        print(f"Hi, am {self.name}")


jhon = Person("Jhon Smith")
print(jhon.name)
jhon.talk()

bob = Person("Bob Smith")
bob.talk()
