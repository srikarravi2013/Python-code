x = input('what is your string')
y = {}

for char in x:
    if char in y:
        y[char] += 1
    else:
        y[char] = 1

for char in x:
    if y[char] == 1:
        print(char)
        break


