# Tuples Immutable
# Tuples Unpackable

numbers = (1, 2, 3, 3)
print(numbers.index(2)) # return index of 2 in list OR ValueError
print(numbers.count(3))

# --------------------------------------- Unpacking
coordinates = (1, 2, 3)

# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# Unpacking
x, y, z = coordinates