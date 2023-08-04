def show_people(peoples):
    for people in peoples:
        print(people)
magicians=['vijay','karthik','arun']
show_people(magicians)

def make_greet(peoples):
    names = []
    while peoples:
        person=peoples.pop()
        print('great magician '+person)
        names.append(person)
    return names
print(make_greet(magicians))