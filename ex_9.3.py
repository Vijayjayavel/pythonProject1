class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print('your first name is '+self.first_name.title())
        print('your last name is '+ self.last_name.title())

    def greet_user(self):
        print('hello, '+self.first_name.title()+' '+self.last_name+' welcome...!')

person=User('vijay','jayavel')

person.describe_user()
person.greet_user()