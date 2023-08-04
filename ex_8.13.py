def profile(firstname,lastname,**infor):
    information={}
    information['firstname']=firstname
    information['lastname']=lastname
    for key,value in infor.items():
       information[key]=value
    return information

user_profile=profile('vijay','jayavel',initial='j',native='vdm',job='ias',age='23')

print(user_profile)
