def fib(x):
        if x<=1:
            return 1
        return fib(x-1)+fib(x-2)
        
        

x = int(input("What is your number? "))
n=0
for n in range(x):
    print(fib(n))
    n+=1
