class Resturant():
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name=resturant_name
        self.cusine_type=cusine_type

    def describe_resturant(self):
        print('the resurant named '+self.resturant_name+' is locted in india')
        print(self.cusine_type + ' in ' + self.resturant_name + ' is so delicious')

    def open_resturant(self):
        print(self.resturant_name+' is open now.')

chennai_Resutrant=Resturant('saravanabavan','idly')
vdm_resturant=Resturant('vijay','poori')
salem_resturant=Resturant('kokkarakko','biriyani')

chennai_Resutrant.describe_resturant()
vdm_resturant.describe_resturant()
salem_resturant.describe_resturant()