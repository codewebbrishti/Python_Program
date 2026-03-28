#print the fibonacci series upto n terms
n:int=int(input("Enter the number of terms: "))
a=0
b=1
if(n==1):
    print(f'The Fibonacci series is: {a}')
elif(n==2):
    print(f'The Fibonacci series is: {a} , {b}')
else:
    print(f'The Fibonacci series is: {a} {b}',end=" ")
    for i in range(3,n+1):
        c=a+b
        print(f'{c}', end=" ")
        a=b
        b=c
print()
#develop a function whether a positive integer belongs to the fibonacci series or not - raise ValueErrors at necessary points
num:int=int(input("Enter the number to be checked: "))
n:int=int(input("Enter the number of terms: "))
fib=[]
a=0
b=1
if(n==1):
    fib=[a]
    print(f'The Fibonacci series is: {a}')
elif(n==2):
    fib=[a,b]
    print(f'The Fibonacci series is: {a} , {b}')
else:
    fib=[a,b]
    print(f'The Fibonacci series is: {a},{b}',end=" ")
    for i in range(3,n+1):
        c=a+b
        fib.append(c)
        print(f'{c}', end=" ")
        a=b
        b=c
print()
def avail_check(num):
    try:
        if(num<=0 or type(num)!=int):
            raise ValueError
        elif num in fib:
            print(f'{num} is present in the fibonacci series')
        else:
            print(f'{num} is not present in the fibonacci series')
    except ValueError:
        return ("Error")
avail_check(num)