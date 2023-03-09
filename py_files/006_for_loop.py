# https://youtu.be/_uQrJ0TkZlc?t=6122
for item in 'Python':
    print(item)

for item in ['Python', 'Java', 'JS']:
    print(item)

for item in [1, 2, 3]:
    print(item)

from_val = 5
to_val = 15
step = 2

for item in range(to_val):
    print(item)

for item in range(from_val, to_val):
    print(item)

for item in range(from_val, to_val, step):
    print(item)

# ----------------------------------------

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(total_price)

# ---------------------------------------- Nested loop

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# ---------------------------------------- Exercise
print("Exercise")
# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     print('x' * num)

numbers = [5, 2, 5, 2, 2]
for num in numbers:
    output = ''
    for count in range(num):
        output += 'x'
    print(output)
