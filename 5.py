#Program to ilustrate datetime module
import datetime
def custom_date():
    day=int(input('Enter the day: '))
    month=int(input('Enter the month: '))
    year= int(input('Enter the year: '))
    date=datetime.date(year, month, day)
    print('The custom date is: ', date)
def custom_time():
    hours=int(input('Enter hours: '))
    minutes=int(input('Enter the minutes: '))
    seconds=int(input('Enter the seconds: '))
    time=datetime.time(hours,minutes,seconds)
    print('The custom time is: ',time)
print('1.Show current system time\n2.Show current system date\n3.Enter custom time\n4.Enter Custom date\n5.Exit')
while True:
    n=int(input('Enter a choice: '))
    if n==1:
        t=datetime.datetime.now()
        t=str(t.hour)+':'+str(t.minute)+':'+str(t.second)
        print('The time now is: ',t)
    elif n==2:
        d=datetime.date.today()
        print('The date is:',d)
    elif n==3:
        custom_time()
    elif n==4:
        custom_date()
    elif n==5:
        print('Thank You!')
        break
    else:
        print('Invalid!')

