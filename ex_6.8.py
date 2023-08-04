pets={'labrador':
      {'owner':'vijay',
       'born':'2000',
       'height':'2'},
      'golden_retriver':
      {'owner':'ajith',
       'born':'2001',
       'height':'3'},
      'puck':
      {'owner':'vijay',
       'born':'2000',
       'height':'2'}}
for dog,dog_info in pets.items():
    print("\ndog name:"+dog)
    print("dog owner's name: "+dog_info['owner'])
    print("dog birth year: " + dog_info['born'])
    print("dog height: " + dog_info['height'])