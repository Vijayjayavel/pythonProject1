import json

def fav(file_name):
    num=input('enter your fav number: ')
    file_name='number.json'
    with open(file_name,'w') as f:
        json.dump(num,f)

def info(file_name):
    filename = 'number.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
        print('i know your fav number is ' + numbers)

file_name='number.json'
fav(file_name)
info(file_name)