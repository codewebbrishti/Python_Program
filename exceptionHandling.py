#Overview of errors or exceptions
#predefined exceptions or run-time errors
  #ValueError
  #TypeError
  #KeyError

#Raising Exception
num:int=int(input("Enter the number: " ))
def sum_n(num):
    if(type(num)!=int or num<=0):
        raise ValueError('Invalid Type or Value')
    res=(num*(num+1))/2
    return res
sum_n(num)

#using try and except for general exception
def sum_n1(num):
    try:
        res=(num*(num+1))/2
        return res
    except:
        print(f'{num} is not a valid integer')
        #raise
        return 0
sum_n1(num)

#handling specific exceptions
def sum_n2(num):
    try:
        if(num<=0 or type(num)!=int):
            raise ValueError
        res=(num*(num+1))/2
        return res
    except ValueError:
        print('Invalid Input')
    except TypeError:
        print('Invalid Input')
    except:
        print(f'{num} is not a valid integer')
        #raise
        return 0
    finally:
        print('With or Without exception')
        return 0
sum_n2(num)

#overview of custom exceptions
class InvalidNumberError(Exception):
    pass 
def sum_n3(num):
    try:
        if(num<=0 or type(num)!=int):
            raise InvalidNumberError
        res=(num*(num+1))/2
        return res
    except InvalidNumberError:
        print('Invalid Input')
    except TypeError:
        print('Invalid Input')
    except:
        print(f'{num} is not a valid integer')
        #raise
        return 0
    finally:
        print('With or Without exception')
        return 0
sum_n3(num)

