file_path='nallai_allai.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())