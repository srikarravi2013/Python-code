def remove_dupe (x):
    unique_list = []
    for num in x:
        if num not in unique_list:
            unique_list.append (num)
    return unique_list   
             



x = []
z = 1

while True:
    try:
        y = int(input(f"what is number {z} in the list (or letters to stop): "))
        x.append(y)
        z += 1 
    except ValueError:
        print(f'the new list is : {remove_dupe(x)}')
        break