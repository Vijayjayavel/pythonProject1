rivers={'egypt':'nile','brazil':'amazon','congo':'congo'}

for con,riv in rivers.items():
    print('the river '+riv+' runs through '+con)
for riv in rivers.values():
    print(riv)
for con in rivers.keys():
    print(con)