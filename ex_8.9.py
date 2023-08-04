def music(art,artist,tracks=''):
    musician={'person':artist,'song':art}
    if tracks:
        musician['tracks']=tracks
    return musician
while True:
    print('enter the album name: ')
    art=input('')
    if art== 'q':
        break
    print('enter artist name: ')
    artist = input('')
    if artist=='q':
        break
    print(art+ ' is composed by '+artist)
