fav_dishes=['idly','dosai','pongal','vadai']
if fav_dishes:
    for fav_dish in fav_dishes:
        if fav_dish == 'idly':
            print('we ran out of idly')
        else:
            print('adding '+ fav_dish+' to you order')
else:
    print('are you sure you want your order cancelled??')