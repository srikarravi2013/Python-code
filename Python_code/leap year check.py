def leap (x):
    if x % 4 == 0:
        return print('its leap')
    if x % 4 != 0:
        return print("its not leap")

x = int(input('what year '))

leap (x)