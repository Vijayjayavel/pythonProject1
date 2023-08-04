books =['polity','geography','economy','socialogy','ethics']
books_1=books[:]
print(books)
print(books_1)
books.append('history')
books_1.append('governance')
print('my books are: ')
for book1 in books:
    print(book1.title())
print('my friend books are: ')
for book2 in books_1:
    print(book2.title())