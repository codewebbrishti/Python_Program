#check whether the year is a leap year or not
year:int= int(input("Enter the year to be checked : "))
if( year<=0 ):
    print('Invalid year has been entered by the user')
else:
    if(year%100 == 0 and year%400 ==0 or year%4==0):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')