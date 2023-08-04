# print eve numbers from a list using lambda function

def eve(l):
    out=list(filter(lambda x:(x%2==0),l))
    return out
print(eve([2,3,4,5,7,8,9,9,12,234,54,54,64,5,786,8,68879,6,8]))
