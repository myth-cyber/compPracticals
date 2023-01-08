def linear(l):
    flag=0
    a=int(input('Enter the element to be searched: '))
    for i in l:
        if i == a:
            flag = 1
            print('Element found')
            break
    if flag != 1:
        print('Element not found')

def bubble(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def minmax(l):
    print('Maximum value is:',max(l))
    print('Minimum value is:',min(l))

def insert(l):
    x=int(input('Enter the element to be inserted: '))
    index=int(input('Enter the index to be added to: '))
    l.insert(index,x)
    return l

def delete(l):
    a=int(input('Enter the element to be deleted: '))
    l.remove(a)
    return l

n=int(input('Enter the limit: '))
l=[int(input('Enter the element: ')) for i in range(n)]
print(l)
while True:
    a=int(input('Enter a choice:\n1.Linear search\n2.Bubble Sort\n3.Minimum and Maximum\n4.Insert an element\n5.Delete an element\n6.Exit\n'))
    if a==1:
        linear(l)
    elif a==2:
        l=bubble(l)
        print(l)
    elif a==3:
        minmax(l)
    elif a==4:
        l=insert(l)
        print(l)
    elif a==5:
        l=delete(l)
        print(l)
    elif a==6:
        print('Thank You')
        break
    else:
        print('Invalid!')