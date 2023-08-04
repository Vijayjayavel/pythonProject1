fav_num={'raj':'1',
         'kumar':{'2','3'},
         'vijay':{'3','1','10','0'},
         'ajith':{'4','8'},
         'surya':{'5','11'}}
for a,b in fav_num.items():
    print('\n' + a.title() + "'s favorite number/s is/are:\t")
    for c in b:
        print('\t'+c)