def music(art,artist,tracks=''):
    musician={'person':artist,'song':art}
    if tracks:
        musician['tracks']=tracks
    return musician

print(music('maryan','arrahman'))
print(music('maryan','arrahman','5'))
