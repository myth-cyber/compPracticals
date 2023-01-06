#Program to check for numeric and string palindrome
def pal_string(s):
    s=s.lower()
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
def pal_num(n):
    num=nrev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    if rev==n:
        print('Palindrome')
    else:
        print('Not Palindrome')
while True:
    n=int(input('Enter a choice:\n1.Check String Palindrome\n2.Check number palindrome\n3.Exit\n'))
    if n==1:
        s=input('Enter String')
        if pal_string(s):
            print("Palindrome")
        else:
            print('Not Palindrome')
    elif n==2:
        number=int(input('Enter Number:'))
        pal_num(number)
    elif n==3:
        print('Thank You')
    else:
        print('Invalid!')
