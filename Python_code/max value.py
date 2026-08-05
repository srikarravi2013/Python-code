def max(x):
    if not x:
        return None        
    maxval = x[0]
    for num in x:
        if num > maxval:
            maxval = num
    return maxval

x = []
z = 1

while True:
    try:
        y = int(input(f"what is number {z} in the list (or letters to stop): "))
        x.append(y)
        z += 1 
    except ValueError:
        print(f'the max number is {max(x)}' )
        break


