class Resturant():
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name=resturant_name
        self.cusine_type=cusine_type

    def describe_resturant(self):
        print('the resurant named '+self.resturant_name+' is locted in india')
        print(self.cusine_type + ' in ' + self.resturant_name + ' is so delicious')

    def open_resturant(self):
        print(self.resturant_name+' is open now.')


chennairesturant=Resturant('anandabavan','idly')
chennairesturant.describe_resturant()
chennairesturant.open_resturant()
