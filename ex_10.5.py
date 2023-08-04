file='guest_list.txt'
print('enter quit when you finish')
while True:
    name = input('enter your name: ')
    if name.title()=='Quit':
         break
    else:
        with open(file, 'a') as f:
             f.write(name)
        print('you are added to the guest list')
        with open(file,'a') as f:
             response=input('why you like python: ')
             f.write('\n'+name+"'s comment about python: "+response+'\n')

