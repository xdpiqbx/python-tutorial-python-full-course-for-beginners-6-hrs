# https://youtu.be/_uQrJ0TkZlc?t=6970

names = ['John', 'Hanna', 'Emmy', 'Bill', 'Sarah']
print(names)
print(names[2])
print(names[-1]) # last item
print(names[2:]) # ['Emmy', 'Bill', 'Sarah']

# It works like Srtings

# ----------------------------------------------- Exercise Find max
print("Exercise")
numbers = [3, 6, 2, 15, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if max < number:
        max = number
print(f'This is max number: {max}')

# ----------------------------------------------- 2D Lists

matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num)

# ----------------------------------------------- Lists functions

# numbers.append(20) # add item to list
# numbers.insert(0, 10) # insert(index_position_in_list, inserted_value)
# numbers.remove(15) # remove value 15 from the list
# numbers.clear() # remove all from list
# numbers.pop() # remove last item from the list
# numbers.index(15) # return index of 15 in list OR ValueError
# print(15 in numbers) # True or False if 15 in list
# numbers.count(4) # return numbers of value 4
# numbers.sort()
# numbers.reverse()
# copied_nums = numbers.copy()

# ----------------------------------------------- Exercise Remove duplicates
print("Exercise")
ex_numbers = [3, 6, 2, 15, 8, 4, 10, 2, 6, 3]
new_list = []
for num in ex_numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)

# ----------------------------------------------- Unpacking
x, y, z, p, l, k, m, n, j, i = ex_numbers
print(f'Unpacking {x} {y} {z}')

# ----------------------------------------------- Split string
string = "Hello world Python here"
print(string.split(" "))
