#calculate the reverse of a number
num:int=int(input("Enter the number: "))
copy=num
rev=0
while num!=0:
    r=num%10
    rev=rev*10+r
    num=num//10
print(f'The reverse of {copy} is {rev}')
if(copy==rev):
    print(f'{copy} is a Palindrome number')
else:
    print(f'{copy} is not a Palindrome number')