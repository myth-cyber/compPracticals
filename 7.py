#Program to write list of strings in a file and copy the strings tat is less that 5 characters to a backup file. Find the number of strings being copied the backupfile
f1_name,f2_name=input('Enter first filename: '),input('Enter second filename: ')
f=open(f1_name,'w')
n=int(input('Enter the number of strings to be written in the file'+f1_name':'))
l=[input('Enter string'str(i+1)+':')+'\n'for i in range(n)]
f.writelines(2)
f.close
f1=open(f1_name)
f2=open(f2_name,'w')
strings=f1.readlines()
for i in strings:
    if len(i.rstrip())<5:
        f2.write(i)
f1.close()
f2.close()

def num_copy(file_name):
    f=open(file_name)
    strings=f.readlines()
    print(len(strings),'string(s) have been copied from',f1_name,'to',file_name)
num_copy()