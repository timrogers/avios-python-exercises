#
# 1a.
#

1 == 1
# => True

#
# 1b.
#

1 != 1
# => False

#
# 1c.
#

(5 + 2) == 7
# => True

#
# 1d.
#

(5 + 2) == '7'
# => False

#
# 1e.
#

2 != (2 - 1)
# => True

#
# 1f.
#

(2 > 1) or (2 < 1)
# => True

#
# 1g.
#

'tim' == 'tim' or 'tim' == 'alice'
# => True

#
# 1h.
#

'tim' == 'tim' and not 'alice' == 'alice'
# => False

#
# 2.
#


def is_negative(number):
    if number < 0:
        # There are other ways you could write this, for example using String's
        # `format` method (Anna's favourite way 😉)
        print(str(number) + " is negative")


print(is_negative(5))
print(is_negative(-1))
# -1 is negative

#
# 3.
#


def is_negative(number):
    # You can also just write `return number < 0`, since this expression
    # evaluates to either `True` or `False`. Clever, huh?
    if number < 0:
        return True
    else:
        return False


print(is_negative(-1))
# => True

#
# 4.
#


def can_redeem(cost_in_avios, total_balance, account_frozen):
    if account_frozen:
        # The member's account is frozen, so they cannot redeem
        return False
    elif cost_in_avios > total_balance:
        # The member doesn't have enough Avios, so they can't redeem
        return False
    else:
        # The member can redeem 🎉 Dusseldorf, here I come!
        return True


# 1. The member has enough Avios, but their account is frozen
print(can_redeem(9000, 9000, True))
# => False

# 2. The member's account isn't frozen, but they don't have enough Avios
print(can_redeem(9000, 8000, False))
# => False

# 3. The member's account isn't frozen AND they have enough Avios 🎉
print(can_redeem(9000, 9000, False))
# => True

#
# 5.
#


def can_redeem(cost_in_avios, total_balance, account_frozen):
    return total_balance >= cost_in_avios and not account_frozen

#
# 6.
#


def can_collect(account_frozen):
    if account_frozen:
        raise ValueError


try:
    can_collect(True)
except ValueError:
    print("The member can't collect 😭")
