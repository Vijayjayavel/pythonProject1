class Resturant():
    def __init__(self,resturant_name,cusine_type,number_served):
        self.resturant_name=resturant_name
        self.cusine_type=cusine_type
        self.number_served=0

    def describe_resturant(self):
        print('the resurant named '+self.resturant_name+' is locted in india')
        print(self.cusine_type + ' in ' + self.resturant_name + ' is so delicious')
    def set_number_served(self):
        print(str(self.number_served)+' has been been served.')

    def incr_number_served(self,numbers):
        self.number_served+=numbers

    def open_resturant(self):
        print(self.resturant_name+' is open now.')
class Icecreamstand(Resturant):

    def __init__(self,resturant_name,cusine_type,number_served):
        super().__init__(resturant_name, cusine_type, number_served)
        self.creams=['vennila','strawberry','padam','pista']

    def creamstand(self):
        for cream in self.creams:
            print(cream)
chennairesturant=Resturant('anandabavan','idly',5)
chennairesturant.describe_resturant()
chennairesturant.number_served=55
chennairesturant.incr_number_served(10)
chennairesturant.set_number_served()
chennairesturant.open_resturant()
flavour=Icecreamstand('vijay','poori',8)
flavour.creamstand()