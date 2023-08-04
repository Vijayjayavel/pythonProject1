a = input('enter the first number: ')
b = input('enter the second number: ')
try:
    c=int(a)+int(b)
except ValueError:
    print('invalid input, enter valid input...!')
else:
    print(c)