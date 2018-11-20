# 1.


def print_greeting(name, age_in_years, address):
    age_in_days = age_in_years * 365
    age_in_years_1000_days_ago = (age_in_days - 1000) / 365

    print("My name is "
          + name + " and I am " + str(age_in_years) + " years old (that's "
          + str(age_in_days) + " days). 1000 days ago, I was "
          + str(age_in_years_1000_days_ago) + " years old. My address is: "
          + address)


address = """WeWork,
38 Chancery Lane,
London,
WC2A 1EN"""

print_greeting("Tim Rogers", 25, address)

# 2.


def square(number=2):
    return number * number


print("Two squared is " + str(square()))
print("Four squared is " + str(square(4)))

# 3.


def powers(number=2):
    squared = number * number
    cubed = number * number * number
    return squared, cubed


five_squared, five_cubed = powers(5)
print(
    "Five squared is " +
    str(five_squared) +
    " and five cubed is " +
    str(five_cubed))
