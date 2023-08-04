favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
must_list=['jen','sarah','edward','phil','james','sam']
for name in must_list:
    if name in favorite_languages.keys():
         print(name.title()+', you already taken the poll')
    else:
        print(name.title()+', you are not taken the poll')