def Details():
    person={}
    person['first_name']=input('enter your fname: ')
    person['last_name']=input('enter your sname: ')
    person['age']=input('enter your age: ')
    person['city']=input('enter your city: ')
    return person

print(Details())