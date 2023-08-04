prompt ='what is your age: '
while True:
    try:
        age = int(input(prompt))
        if age <=3:
            print('your ticket is free')
        elif age <=12:
            print('your ticket is 10 rs')
        elif age > 12:
            print('your ticket is 15 rs')
    except ValueError:
        print('enter a valid input!!!')

