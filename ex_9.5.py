class User():
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0


    def describe_user(self):
        print('your first name is '+self.first_name.title())
        print('your last name is '+ self.last_name.title())

    def loginattemptsprint(self):
        print(str(f'you are logged in {str(self.login_attempts)} times'))

    def incr_login_attempts(self,number):
        self.login_attempts += number
        print('you are logged in ' + str(self.login_attempts) + ' of times')

    def reset_login(self):
        self.login_attempts=0
        print('login attempts: '+str(self.login_attempts))
        print('your login attempts has been reseted')

    def greet_user(self):
        print('hello, '+self.first_name.title()+self.last_name+' welcome...!')

person=User('vijay','jayavel',9)
person.describe_user()
person.login_attempts=100
person.incr_login_attempts(5)
person.greet_user()
person.reset_login()