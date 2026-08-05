def count_digits(n):
    return len(str(abs(n)))

x=int(input('what is your number / string'))
print(count_digits(x))