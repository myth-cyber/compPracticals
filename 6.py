#program to store data in a text file and count no of lines starting with A or a and words that are (and,to,in,the)
def readnumletter():
    count=0
    f=open('data.txt')
    lines=f.readlines()
    for i in lines:
        if i.lower().startswith('a'):
            count+=1
    print('''The number of lines starting with 'A' or 'a' is: ''',count)
def readnumspec():
    d={'and':0,'to':0,'in':0,'the':0}
    f=open('data.txt')
    words=f.read().split()
    for i in words:
        for j in d:
            if i.lower==j:
                d[i]+=1
    f.close()
    print('''The number of 'and' is: ''',d['and'])
    print('''The number of 'to' is: ''', d['to'])
    print('''The number of 'in' is: ''',d['in'])
    print('''The number of 'the' is: ''', d['the'])
f=open('data.txt','w')
n=int(input('Enter the number of lines to be written to the file data.txt: '))
d=[input('Enter the string of line '+str(i+1)+':')+'\n'for i in range(n)]
f.writelines()
f.close()
print('1.Count the occuerence of and, to, in, the in the text file\n2.Count the number of lines starting with A or a in the text file\n3.Exit')
while True:
    n=int(input('Enter a choice: '))
    if n==1:
        readnumspec()
    elif n==2:
        readnumletter()
    elif n==3:
        print('Thank You!')
    else:
        ('Invalid!')
        




