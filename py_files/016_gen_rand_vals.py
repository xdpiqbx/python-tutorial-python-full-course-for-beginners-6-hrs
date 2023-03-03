import random

for i in range(15):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

random.random()  # example 0.027964642254873495
random.randint(10, 20)  # random in range 10 to 20


# ------------------------------------------------
class Dice:
    def roll(self):
        tuple = (random.randint(1, 6), random.randint(1, 6))
        return tuple

dice = Dice()
print(dice.roll())
