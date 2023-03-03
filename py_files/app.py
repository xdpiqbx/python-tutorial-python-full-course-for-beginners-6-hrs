# print("Start !!!")
# print('o----')
# print(' ||||')
# print('*' * 10)

# ========================= Variables =========================

# price = 10
# raring = 4.9
# name = 'Artem'
# isValid = True
#
# full_name = input('Name? ')
# print('Hi ' + full_name)

# ============================================================ global
# x = 50
# def func():
#     global x
#     print('x =', x)
#     x = 2
#     print('Заменяем глобальное значение x на', x)
# func()
# print('Значение x составляет', x)

# ============================================================ nonlocal
def func_outer():
    x = 2
    print('x равно', x)  # x равно 2
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x) # Локальное x сменилось на 5


func_outer()
# ========================== Cast type

# int(10)
# float(4.5)
# str("Name")
# type(10)
#
# birth_year = input('Year: ')
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)
