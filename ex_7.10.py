data={}
active=True
while active:
    print('what is your name: ')
    name=input()
    print('if you could visit a place in a world where would you go?: ')
    place=input()
    print('would you like to continue the poll: yes/no ?')
    response=input()
    data[name]=place
    if response.lower() == 'no':
        active=False
for name,place in data.items():
    print(data)


