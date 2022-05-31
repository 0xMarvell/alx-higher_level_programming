#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num_str = repr(number)[-1]
last_digit = int(num_str)

if last_digit > 5:
    str = "and is greater than 5"
    print(f"Last digit of {number} is {last_digit} {str}")
elif last_digit < 6 and last_digit != 0:
    str = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} {str}")
elif last_digit == 0:
    str = "and is 0"
    print(f"Last digit of {number} is {last_digit} {str}")
else:
    print(f"Last digit of {number} is {last_digit}")
