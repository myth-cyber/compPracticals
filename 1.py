from random import randint

def binary(l,x):
    low= 0
    high = len(l) - 1 
    mid = 0
    while low <= high:
        mid = (low+high) // 2
        if l[mid] == x:
            return mid
        elif x < l[mid]:
            high = mid - 1
        elif x > l[mid]:
            low = mid + 1
    return None
n=int(input('Enter the no. of elements of the list: '))
l=[randint(0,100) for i in range(n)]
l.sort()
print(l)
x=int(input('Enter the number to be searched: '))
index=binary(l,x)
if index != None:
    print('Element found at index:',index)
else:
    print('Element not found')