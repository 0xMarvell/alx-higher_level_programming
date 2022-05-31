#!/usr/bin/python3

def print_last_digit(number):
    num_str = repr(number)[-1]
    last_digit = int(num_str)

    print(last_digit)
