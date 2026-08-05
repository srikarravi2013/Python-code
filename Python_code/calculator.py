def add (x,y):
    return x+y
def subtract (x,y):
     return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y

num1 = int(input ('first number '))
num2 = int(input ('second number'))
function = input ("function ")


if function == 'divide':
    print(divide(num1,num2))
if function == 'add':
    print(add(num1,num2))
if function == 'subtract':
    print(subtract(num1,num2))
if function == 'multiply':
    print(multiply(num1,num2))


