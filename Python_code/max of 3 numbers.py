def max(x, y, z):
    numbers = [x, y, z]
    maxval = numbers[0]
    for num in numbers:
        if num > maxval:
            maxval = num
    print(maxval)


x = int((input('first num: ')))
y = int((input('second num: ')))
z = int(input('third num: '))

max(x,y,z)