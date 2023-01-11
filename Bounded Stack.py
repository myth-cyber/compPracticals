def emp_display(stack):
    if stack==[]:
        print("Stack Underflow")
    else:
        for i in range (len(stack)-1,-1,-1):
            print(stack[i])
def emp_pop(stack):
    if not stack:
        print("Stack Underflow")
        top=-1
    else:
        print("Element deleted from the stack is ",stack.pop())
        if len(stack)==0:
            top=-1
        else:
                top=len(stack)-1
def emp_peek(stack):
    if not stack:
        print("Stack Underflow")
    else:
        top=len(stack)-1
        print(stack[top])
def emp_push(stack):
    stack_count=len(stack)
    if stack_count>=maxsize:
        print("Stack Overflow")
        top=len(stack)-1
    else:
        E_id=int(input("Enter Employee ID: "))
        Ename=input('Enter Employee Name: ')
        Sal=int(input('Enter Employee Salary: '))
        Desig=input('Enter Employee Designation: ')
        Exp=int(input("Enter Employee year's of experience: "))
        temp=[E_id,Ename,Sal,Desig,Exp]
        stack.append(temp)
        top=len(stack)-1
stack=[]
maxsize=5
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Peek")
    print("5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        emp_push(stack)
    elif ch==2:
        emp_pop(stack)
    elif ch==3:
        emp_display(stack)
    elif ch==4:
        emp_peek(stack)
    elif ch==5:
        print("Exiting...")
        break
    else:
        print('Invalid Choice!')
