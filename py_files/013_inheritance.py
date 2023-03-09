class Animal:
    alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is Eating...")

    def sleep(self):
        print(f"{self.name} is Sleeping...")


class Rabbit(Animal):
    def run(self):
        print(f"{self.name} Running")


class Fish(Animal):
    def swim(self):
        print(f"{self.name} Swimming")


class Hawk(Animal):
    def fly(self):
        print(f"{self.name} Flying")


rabbit = Rabbit("Rabbit")
fish = Fish("Fish")
hawk = Hawk("Hawk")

print(rabbit.eat())
# print(rabbit.sleep())
# print(rabbit.run())
