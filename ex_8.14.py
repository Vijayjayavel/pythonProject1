def cars(modelname,manufacturer,**other):
    model={}
    model['modelname']=modelname
    model['manufacturer']=manufacturer
    for key,values in other.items():
        model[key]=values
    return model
vehicle=cars('bmw','airbus',year='2022',mil='200')
print(vehicle)

