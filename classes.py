# A class is a blueprint for creating objects. Everything in Python is an object.

class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def hasBirthday(self):
        self.age += 1

# init user object
ryan = User('Ryan Brooks', 'ryan@gmail.com', 40)

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_Balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#Init customer

janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_Balance = 500

print(ryan.greeting())

print(ryan.hasBirthday())