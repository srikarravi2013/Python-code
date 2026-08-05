def exponent(x,n):
    if x== 0:
     return 0
    elif n == 0:
     return 1
    else:
     return x*exponent(x,n-1)

x = int(input('what is your base: '))
n = int(input('what is your exponent: '))

print(exponent(x,n))
   