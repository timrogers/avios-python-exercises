# 3. Control Flow

1. Would the following expressions be `True` or `False`?

   Try guessing yourself, and then try for yourself [here](https://repl.it/languages/python3), by typing each expression into the black panel on the right and then pressing "Enter" to see the answer.

```python
# 1a.
1 == 1

# 1b.
1 != 1

# 1c.
(5 + 2) == 7

# 1d.
(5 + 2) == '7'

# 1e.
2 != (2 - 1)

# 1f.
(2 > 1) or (2 < 1)

# 1g.
'tim' == 'tim' or 'tim' == 'alice'

# 1h.
'tim' == 'tim' and not 'alice' == 'alice'
```


2. Write a function, `is_negative()`, which takes one number as an argument and checks whether that number is negative. If it is negative, then the function should print "<insert number here> is negative", for example, "-1 is negative".

   Try the function out with a negative and positive number to see if it works.

3. Re-write your function to *return* a boolean variable signifying whether the number is negative. Call that function with a negative number, and print what is returned.

4. Write a function, `can_redeem()`, which takes three arguments -- `cost_in_avios`, `total_balance` and `account_frozen` -- and returns whether the member can redeem for flights costing `cost_in_avios` Avios.

   You'll need to check if the member's account is frozen, and then if they have enough Avios.
   
   Try that function out, checking that all of the different cases work as expected.

5. Think back to question 4. Is there any way you can make this code simpler or cleaner? It's possible to write this function in one line, thanks to the magic of `and not`.

6. Write a function, `can_collect()`, which takes a single `account_frozen` argument, checks if the account is frozen, and raises a `ValueError` if the account if frozen.

   Try calling that function, using the `except` statement to "catch" the `ValueError` and print a nice message.

You can find the solutions [here](https://github.com/timrogers/avios-python-exercises/blob/master/3_control_flow/solution.py).
