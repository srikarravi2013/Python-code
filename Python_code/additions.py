def addition(y, x):
    total = 0
    while x > y:
        total += x
        x -= 1
    print(total)

x = int(input("What is your number? "))
addition(1, x)