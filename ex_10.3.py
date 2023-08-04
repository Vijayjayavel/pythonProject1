file_path='guest.txt'

with open(file_path,'w') as file:
    name=input('enter your name: ')
    file.write(name)

with open(file_path,'r') as file:
    for line in file:
        print(line.strip())