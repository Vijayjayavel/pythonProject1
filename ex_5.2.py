print('what is your name:')
user = input()
if user.lower() != "vijay":
    print('\nfuck off\n')
else:
    print('\nwelcome chief')
print('\nwhat is your age:')
age = int(input())
if age >= 18:
    print('\nyou are allowed to apply for this exam')
else:
    print('\nyou cant apply for this exam')
list=['vijay','ajith','rajini','kamal']
if user not in list:
    print('\nyou are not in the eligible list')
else:
    print('\nyou are in the eligible list')