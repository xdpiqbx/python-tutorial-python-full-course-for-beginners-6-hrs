# https://youtu.be/_uQrJ0TkZlc?t=8319

customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}

print(customer.items()) # dict_items([('name', 'John'), ('age', 30), ('is_verified', True)])
print(customer.values()) # dict_values(['John', 30, True])
print(customer.keys()) # dict_keys(['name', 'age', 'is_verified'])

customer["birthday"] = "Jan 1 1980" # Add new field to dict

for key in customer.keys():
    print(customer[key])

# --------------------------------- Exercise

nums = {
    '0': "Zero",
    '1': "==1==",
    '2': "==2==",
    '3': "==3==",
    '4': "==4==",
    '5': "==5==",
    '6': "==6==",
    '7': "==7==",
    '8': "==8==",
    '9': "==9==",
}

phone = input("Phone: ")
str = ""
for digit in phone:
    str += nums.get(digit, "!") + " "
print(str)

# --------------------------------- Smile converter
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)