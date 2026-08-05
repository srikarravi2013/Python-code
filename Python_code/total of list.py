def total(x):
    total = 0
    for num in x:
        total += num
    print(total) 


x = []
z = 1

while True:
    try:
        y = int(input(f"what is number {z} in the list (or letters to stop): "))
        x.append(y)
        z += 1 
    except ValueError:
        total(x)
        break