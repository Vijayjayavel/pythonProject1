books =['polity','geography','economy','socialogy','ethics']
print('the first three items in the list are:')
for book1 in books[:3]:
    print('                               \t '+ book1)
print('\nthe middle three items of the list:')
for book2 in books[1:4]:
    print('                               \t '+ book2)
print("\nthe last three items of the list: \t")
for book3 in books[-3:]:
    print('                               \t '+ book3)