import json

try:
    with open('numberss.json') as file:
        number=json.load(file)
except FileNotFoundError:
    number=input('enter your fav number: ')
    with open('numberss.json','w') as file:
        json.dump(number,file)
    print('ill remember the number..!')
else:
    print('i know your fav number is '+ number)