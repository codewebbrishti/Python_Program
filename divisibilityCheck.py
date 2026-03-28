#check if the number entered by the user is a positive integer and divisible by 2 or 3
num:int= int(input("Enter the number from the user: "))
if((type(num)==int and num>0)):
    print(f'{num} is a positive integer')
if(num%2==0):
    print(f'{num} is divisible by 2')
elif(num%3==0):
    print(f'{num} is divisible by 3')
else:
    print(f'{num} is not a positive integer')