# if elif else
# and or not
# > < == <= >= !=

is_hot = False
is_cold = True

if is_hot:
    print("Drink water")
    print("Hot now")
elif is_cold:
    print("It's cold now")
else:
    print("Enjoy your day")

# =========== Example 1 =========== # if elif else
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")

# =========== Example 2 =========== # and or
has_high_income = True
has_good_credit = True
has_criminal_record = False

if (has_high_income or has_good_credit) and not has_criminal_record:
    print("Eligible for loan")

# =========== Example 3 =========== # > < == <= >= !=
temperature = 33
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# =========== Example 4 ===========
name = 'John'
if len(name) < 3:
    print("to short")
elif len(name) > 50:
    print("to long")
else:
    print("OK!")
