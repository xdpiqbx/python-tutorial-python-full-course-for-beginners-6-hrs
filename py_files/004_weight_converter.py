# https://youtu.be/_uQrJ0TkZlc?t=4654
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ').upper()
if unit == 'L':
    print(f"You are {weight * 0.45} kilos")
elif unit == 'K':
    print(f"You are {weight // 0.45} lbs")
else:
    print(f"Unit [{unit}] is unacceptable")
