#progrram to store details of objeccts books in binary file and perform search upadtae deleteion. Data is stored in form of list with detials bookid book name author price
import pickle
def read():
    records=[]
    f=open('book.dat','rb')
    try:
        while True:
            a=pickle.load(f)
            records.append(a)
    except EOFError:
        pass
    f.close()
    return records

def write(records):
    f=open('book.dat','wb')
    for in in records:
        pickle.dump(i,f)
    f.close()

def search():
    flag=False
    bookname=input('Enter the name of the book to search for: ')
    books=read()
    for i in books:
        if bookname==i[1]:
            flag=True
            print('Book Found!')
            break
    if flag==False:
        print('Book not Found!')
def update():
    bookname=input('Enter the name of the book whose price is to be updated')
    flag=-1
    books=read()
    for i in range(len(books)):
        if books[i][1]==bookname:
            flag=i
            break
    if flag!=-1:
        price=int(input('Enter the updated price: '))
        books[i][3]=price
        write(books)
        print('Updated!')
        return None
    print('Error! no such book')

def delete():
    bookname=input('Enter the name of the book to be deletd: ')
    flag=False
    books=read()
    for i in books:
        if bookname==i[1]
            flag=True
            books.remove(i)
            print('Deleted!')
            break
    if flag==False:
        print('Error! no such booK')
        return None
    write(books)

def display():
    books=read()
    if not books:
        print('Empty')
    for i in books:
        print(i)

def main():
    n=int(input('Enter the limit: '))
    books=

