while True:
    a = input('enter the first number: ')
    if a=='q':
        break
    b = input('enter the second number: ')
    try:
         c=int(a)+int(b)
    except ValueError:
        print('addition of string and numerical not possible enter valid input...!')
    else:
        print(c)
