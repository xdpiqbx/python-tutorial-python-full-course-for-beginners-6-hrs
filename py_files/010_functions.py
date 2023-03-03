def greet_user(first_name="user", last_name="default"):
    print(f"Hello {first_name} {last_name}!")


greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
# greet_user(last_name="Smith", "John") # Error
greet_user("John")
greet_user()


# ---------------------------------------------------------------
def square(number):
    return number * number


print(square(3))


# ---------------------------------------------------------------
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))


# ---------------------------------------------------------------

def total(initial=5, *numbers, **keywords):
    # *numbers - all params to Tuple
    # **keywords - all params to Dict
    count = initial
    for number in numbers:
        print(number)
        count += number
    for key in keywords:
        print(key)
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, vegetables=50, fruits=100))
