dosai=['masal dosai','podi dosai','onion dosai','rava dosai','masal dosai','masal dosai']

finished = []
while dosai:
    order = dosai.pop()
    print('i made your '+order+' order')
    finished.append(order)
print('\nyour orders are:')
for order in finished:
    print('\t'+order)
