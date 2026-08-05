def generate_a_list():
    x = []
    z = 1
    print('type a list from 1-100: ')

    while True:
        try:
            y = int(input(f"what is number {z} in the list (or letters to stop): "))
            x.append(y)
            z += 1 
        except ValueError:
            break
    return x

a = generate_a_list()
b = int(input('what is your max value: '))

for i in range (1, b):
    if i not in a:
        print (i)
    
    