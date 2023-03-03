# Text Type:        str
# Numeric Types:    int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:     dict
# Set Types:        set, frozenset
# Boolean Type:     bool
# Binary Types:     bytes, bytearray, memoryview
# None Type:        NoneType

# x = ["apple", "banana", "cherry"]  - list
# x = ("apple", "banana", "cherry") - tuple
# x = {"name" : "John", "age" : 36} - dict
# x = {"apple", "banana", "cherry"} - set
# x = frozenset({"apple", "banana", "cherry"}) - frozenset

# type(x) - to get type

class Point:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.z = 30  # also you cat create

print(point1.x)
print(point1.y)
point1.draw()


# point2 = Point()
# print(point2.z) # print(point2.x) AttributeError: 'Point' object has no attribute 'x'
# point2.draw()

# -------------------------------------------------------------------------------------

class Person:
    def __init__(self, name):  # constructor
        self.name = name

    def talk(self):
        print("I am talking")

person = Person("John")
print(person.talk())
print(person.name)

# https://youtu.be/_uQrJ0TkZlc?t=11616