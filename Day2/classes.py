
# Create a Car Class
class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def start(self):
        print("The car has Started!")

    def stop(self):
        print("The car has stopped!")


car1 = Car("Tata", "Blue", "NZ5001")
car1.start()
car1.stop()

# Create a BankAccount Class


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance : {self.balance}")


account1 = BankAccount("Nandhini", 1400000)
account1.show_balance()
account1.deposit(100000)
account1.withdraw(1700000)
account1.show_balance()


class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def promote(self, new_position, raise_amount):
        self.position = new_position
        self.salary += raise_amount

    def show_details(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Position : {self.position}")
        print(f"Employee salary : {self.salary}")


employee1 = Employee("Nandhini", 33, "IoT Software Design Engineer", 100000)
employee1.show_details()
employee1.promote("Full Stack Developer", 3000000)
employee1.show_details()

# inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child Class


class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")


# Creating objects
dog = Dog("Bruno")
dog.speak()  # From Animal
dog.bark()
