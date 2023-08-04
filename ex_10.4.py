

file='guest_list.txt'
print('enter quit when you finish')
while True:
    name = input('enter your name: ')
    if name.title()=='Quit':
         break
    else:
        with open(file, 'a') as f:
             f.write(name+'\n')
        print('you are added to the guest list')

