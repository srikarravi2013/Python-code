def table(x, y):
    print(f"Multiplication Table for {x}:")
    for i in range(1, y + 1):
        result = x * i
        print(f"{x} x {i} = {result}")

x=int(input('number'))
y=int(input('up to:'))

table(x, y)