def count(x):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in x:
        if char in vowels:
            count += 1
            
    return count

x=input('what is your string')

print(count(x))