#!/usr/bin/python3

for num in range(0, 90):
    if num % 10 > num / 10:
        if num != 89:
            print(f"{num:02}, ", end="")
        else:
            print(f"{num:02}")
#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (True)
    else:
        return (False)