import math

def prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
            
    return True

x=int(input('what is your number'))

print(prime(x))