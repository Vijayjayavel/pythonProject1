friends = ['siva','rajesh','sakthivel']

print(friends[0].title() + ' sapda variya da')
print(friends[1].title() + ' sapda variya da')
print(friends[2].title() + ' sapda variya da')

print(friends[2].title() + ' la vara mudila')
friends[2] = 'vijay'
print(friends[0].title() + ' sapda variya da')
print(friends[1].title() + ' sapda variya da')
print(friends[2].title() + ' sapda variya da')
friends.append('janani')
friends.insert(0,'karthi')
print(friends[0].title() + ' sapda variya')
print(friends[1].title() + ' sapda variya')
print(friends[2].title() + ' sapda variya')
print(friends[3].title() + ' sapda variya')
print(friends[4].title() + ' sapda variya')

del friends[0]
print(friends)
poped_friends=friends.pop(-1)
print(friends)
print(poped_friends)
print(sorted(friends))
friends.sort()
friends.sort(reverse=True)
print(friends)