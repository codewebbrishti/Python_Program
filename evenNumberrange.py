#even number range 
n:int= int(input("Enter the number of elements to be printed: "))
print(f'The list of even numbers in the range 1 to {n} are: ')
def even_num(n:int)-> None:
    l=range(1,n+1)
    for i in l:
        if(i%2==0):
           res=i
           print(f'{res}')
even_num(n)