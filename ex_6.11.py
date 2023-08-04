cities={'delhi':
            {'state':'newdelhi',
             'pop':'180 lakh',
             'fact':'capital'},
        'mumbai':
            {'state':'maharashtra',
             'pop':'240 lakh',
             'fact':'capital'},
        'chennai':
            {'state':'newdelhi',
             'pop':'160 lakh',
             'fact':'capital'}}
for a,b in cities.items():
    print('\nname of the city is: \n\t'+a)
    print('state of the city: \n\t'+b['state'])
    print('population of the state is: \n\t'+b['pop'])
    print('one fact about the city:\n\t'+b['state']+' is '+b['fact']+' of the state')

