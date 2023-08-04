print('***enter break to stop the program***\n')
while True:
    user=input('enter your user name: ')
    if user.lower()=='vijay':
        print('hello chief do you want to see the status report..??')
    elif user.lower()=='break':
        break
    else:
        print(f'hello {user} thank you for logging in again...!!!')
