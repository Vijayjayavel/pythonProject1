
def files_open(files):
    try:
        with open(files) as f:
            contents=f.read()
    except FileNotFoundError:
        print('entered file not found')
    else:
        words=contents.split()
        for file in words:
            print(file)


files=['dog.txt','cats.txt','nallai_allai.txt','gowtham.txt']
for file in files:
    files_open(file)