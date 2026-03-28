#accept the range (value of n) and print only the numbers which are greater than 100
n:int=int(input("Enter the upper bound: "))
l=list(range(0,n+1))
i=0
print(f'The numbers greater than 100 in the range (0 to {n}) are: ')
while i<len(l):
    if(l[i]>100):
        print(f'{l[i]}')
    i+=1
#enter positive integer to add and non positive integer to exit: if num=0 , continue without adding to sum
sum=0
print('Enter positive integer to add and non positive integer to exit')
while True:
    num:int=int(input("Enter the integer: "))
    if(num==0):
        continue
    if(num.is_integer and num>0 ):
        sum+=num
    else:
        print('Code Terminated as negative number is entered')
        break
print(f'Sum is : {sum}')

#accept the range (value of n) and print only the sum of the numbers which are greater than 100 (increment the numbers by 5)
n:int=int(input("Enter the upper bound: "))
l=list(range(0,n+1,5))
i=0
res=0
print(f'The numbers greater than 100 in the range (0 to {n}) are: ')
while i<len(l):
    if(l[i]>100):
        res+=l[i]
    i+=1
print(f'Sum of the numbers greater than 100 is: {res}')

#print all the numbers which are divisible by both 2 and 3 in the range 1 to n
n:int=int(input("Enter the upper bound: "))
l=list(range(1,n+1))
print('The numbers which are divisible by both 2 and 3 are: ')
for i in l:
    if(i%2==0 and i%3==0):
        print(f'{i}')