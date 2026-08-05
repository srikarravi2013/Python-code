import random

def guess():
    x = random.randint(1, 100)
    print('welcome to the number guessing game')
    print('i have picked a number 1-100 try to guess it:')

    tries = 0

    while True:
            try:
                y = int(input('what is your guess: ')) 
                tries += 1                
                if y < x:
                    print("too low! Try again.")
                elif y > x:
                    print("too high! Try again.")
                else:
                    print(f"correct! It took you {tries} tries.")
            except ValueError:
                 print('enter a valid number')

                
guess()    