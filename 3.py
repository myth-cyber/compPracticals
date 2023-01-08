def create():
    d={}
    n=int(input('Enter the number of students: '))
    for i in range(n):
        x=input('Enter the admission number of the student: ')
        name=input('Enter the name of the student: ')
        division=input('Enter the class of the student: ')
        Class=input('Enter the division of the student: ')
        d[x]=[name,division,Class]
        return d

def search(d):
    x=input('Enter the admission number of the student: ')
    if x in d:
        print('Student found')
    else:
        print('Student not found')

def display(d):
    print(d)

def update(d):
    x=input('Enter the admission number of the student: ')
    name=input('Enter the update name of the student: ')
    