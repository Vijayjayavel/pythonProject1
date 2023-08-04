class User():
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts

    def describe_user(self):
        print('your first name is '+self.first_name.title())
        print('your last name is '+ self.last_name.title())

    def incr_login_attempts(self,num):
        self.login_attempts+=num
        print('you are logged in ' + str(num) + ' of times')

    def reset_login(self):
        self.login_attempts=0
        print('login attempts: '+str(self.login_attempts))
        print('your login attempts has been reseted')

    def greet_user(self):
        print('hello, '+self.first_name.title()+self.last_name+' welcome...!')

class Privileges():
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges=['can ban user','can add post','can del post']





person=User('vijay','jayavel',9)
person.describe_user()
person.greet_user()
person.incr_login_attempts(2)
person.reset_login()
rock=Privileges('vijay','jaya',4)
print('admin privileges are the following below: \t')
rock.show_privileges()